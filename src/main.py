#!/usr/bin/python3

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

import rtmidi.midiutil as midiutil
import time

from setup import initialize

from midi_in.Trigger import *
from midi_in.InputLogger import InputLogger

from strip_utils import clear_LEDs
from gamma_correction import *

from rpi_ws281x import *

import threading

from actions.Action import Action

LED_COUNT = 109
# LED_COUNT = 60
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
def index():
	print(application.get_payload())
	return render_template('index.html', data=application.get_payload())

class App:
	def add_trigger(self, trigger):
		self.triggers[trigger.key].append(trigger)
		trigger.action.set(trigger.control, trigger.bounds[0], self.params)
		self.inputLogger.add_trigger(trigger)
		if trigger.action not in self.actions:
			self.actions.append(trigger.action)

	def add_entity(self, entity):
		self.entities.append(entity)

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
		self.entities = []

		initialize(self, self.params)

		strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
		strip.begin()

		clear_LEDs(strip, self.params["LEDCount"])
		strip.show()

		# initialize midi
		print("Initializing MIDI")
		midiutil.list_input_ports()
		midiin, port_name = midiutil.open_midiinput(1)
		midiin2, port_name = midiutil.open_midiinput(2)
		midiin.set_callback(self)
		midiin2.set_callback(self)

		print("Ready...")
		# Main loop
		while True:
			start = time.time()

			clear_LEDs(strip, self.params["LEDCount"])

			# Update
			for triggers in self.triggers:
				for trigger in triggers:
					if trigger.state != TriggerStates.Idle:
						trigger.update(self.params)

			entity_remove_list = []
			for entity in self.entities:
				entity.update(self.params)
				if entity.finished:
					entity_remove_list.append(entity)

			for entity in entity_remove_list:
				self.entities.remove(entity)


			for action in self.actions:
				if action.is_on():
					action.update(self.params)

			# Render
			for action in self.actions:
				if action.is_on():
					action.render(self.params, strip)

			for entity in self.entities:
				entity.render(self.params, strip)

			for action in self.actions:
				if action.is_on():
					action.render_post(self.params, strip)

			correct_gamma(strip, self.params)
			
			strip.show()

			time_dif = time.time() - start
			if time_dif < 0.016:
				time.sleep(0.016 - time_dif)
			# print(time.time() - start)

		print("Goodbye!")

	def get_payload(self):
		return {
			"actions": list(map(Action.to_dict, self.actions)),
			"triggers": [list(map(Trigger.to_dict, x)) for x in self.triggers]
		}

	def __call__(self, event, data=None):
		message, deltatime = event

		state    = message[0]
		key      = message[1]
		velocity = message[2]/128

		if state == 128:
			velocity = 0

		# print(state, key, velocity)

		for map_key, triggers in enumerate(self.triggers):
			for trigger in triggers:
				if(map_key == key):
					if trigger.type == TriggerTypes.Key or trigger.type == TriggerTypes.Toggle:
						if velocity > 0:
							trigger.trigger(self, self.params, velocity)
						else:
							trigger.key_up(self.params)
					elif trigger.type == TriggerTypes.Knob:
						trigger.knob(self.params, velocity)


if __name__ == '__main__':
	application = App()
	thread = threading.Thread(target=application.main)
	thread.start()
	app.run(debug=True, host='0.0.0.0', port=8085, use_reloader=False)