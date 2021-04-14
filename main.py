#!/usr/bin/python3

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

import rtmidi.midiutil as midiutil
import time

from setup import initialize

from midi_in.Trigger import *
from midi_in.InputLogger import InputLogger

from gamma_correction import *

from rpi_ws281x import *

import threading

from actions.Action import Action

LED_COUNT = 119
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0

app = Flask(__name__)
bootstrap = Bootstrap(app)

application = None

@app.route('/')
def hello_world():
	print(application.get_payload())
	return render_template('index.html', data=application.get_payload())

class App:
	def addTrigger(self, trigger):
		self.triggers[trigger.key].append(trigger)
		self.inputLogger.addTrigger(trigger)
		if trigger.action not in self.actions:
			self.actions.append(trigger.action)

	def main(self):
		print("Starting py-lights...")

		self.params = {
			"MAX": 255,
			"LEDCount": LED_COUNT,
			"KeyCount": 128
		}

		self.inputLogger = InputLogger()

		self.triggers = []
		for i in range(self.params["KeyCount"]):
			self.triggers.append([])

		self.actions = []


		initialize(self, self.params)

		strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
		strip.begin()

		for x in range(0, LED_COUNT):
			strip.setPixelColor(x, Color(0, 0, 0))
		strip.show()

		# initialize midi
		print("Initializing MIDI")
		midiin, port_name = midiutil.open_midiinput(1)
		midiin.set_callback(self)

		print("Ready...")
		# Main loop
		while True:

			t = time.process_time()

			for key, triggers in enumerate(self.triggers):
				for trigger in triggers:
					if trigger.state != TriggerStates.Idle:
						trigger.update(self.params)

			for action in self.actions:
				action.update(self.params)

			for i in range(0, LED_COUNT):
				strip.setPixelColor(i, Color(0, 0, 0))

			for action in self.actions:
				action.render(self.params, strip)

			for action in self.actions:
				action.render_mask(self.params, strip)

			correct_gamma(strip, self.params)

			strip.show()

		print("Goodbye!")

	def get_payload(self):
		return {
			"actions": list(map(Action.to_dict, self.actions)),
			# "triggers": list(map(Trigger.to_dict, self.triggers))
			"triggers": [list(map(Trigger.to_dict, x)) for x in self.triggers]
		}
		# return {
		# "actions": [
		# 	{
		# 		"name": "test1",
		# 		"type": "Color",
		# 		"parameters": [
		# 			{
		# 				"name": "Color",
		# 				"value": "#FF0000",
		# 				"type": "COLOR"
		# 			}
		# 		],
		# 		"settings": [
		# 			{
		# 				"name": "Volume",
		# 				"value": 1,
		# 				"type": "PERCENTAGE"
		# 			}
		# 		]
		# 	},
		# 	{
		# 		"name": "test2",
		# 		"type": "Color",
		# 		"parameters": [
		# 			{
		# 				"name": "Color",
		# 				"value": "#FF0000",
		# 				"type": "COLOR"
		# 			}
		# 		],
		# 		"settings": [
		# 			{
		# 				"name": "Volume",
		# 				"value": 0.5,
		# 				"type": "PERCENTAGE"
		# 			}
		# 		]
		# 	}
		# ]
	# }

	def __call__(self, event, data=None):
		message, deltatime = event

		state    = message[0]
		key      = message[1]
		velocity = message[2]/128

		if state == 128:
			velocity = 0


		for mapKey, triggers in enumerate(self.triggers):
			for trigger in triggers:
				if(mapKey == key):
					if trigger.type == TriggerTypes.Key:
						if velocity > 0:
							trigger.trigger(self.params, velocity)
						else:
							trigger.keyUp(self.params)
					elif trigger.type == TriggerTypes.Knob:
						trigger.knob(self.params, velocity)


if __name__ == '__main__':
	application = App()
	thread = threading.Thread(target=application.main)
	thread.start()
	app.run(debug=True, host='0.0.0.0', port=8085)