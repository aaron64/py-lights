import rtmidi.midiutil as midiutil
import time

from setup import initialize

from midi_in.Trigger import Trigger, TriggerStates
from midi_in.InputLogger import InputLogger

from rpi_ws281x import *

LED_COUNT = 60
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0

strip = None

class App:
	def addTrigger(self, trigger):
		self.triggers[trigger.key].append(trigger)
		self.inputLogger.addTrigger(trigger)
		if trigger.action not in self.actions:
			self.actions.append(trigger.action)

	def main(self):
		global strip
		print("Starting py-lights...")

		self.params = {
			"MAX": 255,
			"LEDCount": LED_COUNT,
			"KeyCount": 128,
			"Counter": 1,
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
			self.params["Counter"] += 1

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

			# for key, trigger in self.triggers.items():
			# 	if trigger.settings["MUTE"] == True:
			# 		self.params["VISIBILITY"] = 0
			
			strip.show()
			time.sleep(0.00001)

		print("Goodbye!")

	def __call__(self, event, data=None):
		message, deltatime = event

		print(message)
		state    = message[0]
		key      = message[1]
		velocity = message[2] * 2

		for mapKey, triggers in enumerate(self.triggers):
			for trigger in triggers:
				if(mapKey == key):
					if velocity > 0:
						print(strip)
						trigger.trigger(self.params, strip)
					else:
						trigger.keyUp(self.params)

App().main()
