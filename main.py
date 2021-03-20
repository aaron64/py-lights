# import rtmidi.midiutil as midiutil
import time

# from setup import initialize

from midi_in.InputControl import InputControl
from midi_in.InputLogger import InputLogger

from rpi_ws281x import *

LED_COUNT = 10
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0

class App:
	def addAction(self, action):
		self.actions.append(action)
		return action

	def addInput(self, action, type, key, setting):
		midiInput = InputControl(action, type, key, setting)
		self.inputs.append(midiInput)
		self.inputLogger.addInput(midiInput)

	def main(self):
		print("Starting py-lights...")

		self.params = {
			"MAX": 255, 
			"Counter": 1,
		}

		self.inputLogger = InputLogger()

		self.actions = []
		self.inputs = []

		# initialize(self, self.params)       

		strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
		strip.begin()

		for x in range(0, LED_COUNT):
			strip.setPixelColor(x, Color(0, 25 * x, 250 - 25 * x))
		strip.show()

		# initialize midi
		print("Initializing MIDI")
		# midiin, port_name = midiutil.open_midiinput(1)
		# midiin.set_callback(self)

		print("Ready...")
		# Main loop
		while True:
			self.params["Counter"] += 1

			for action in self.actions:
				action.update(self.params)

			for action in self.actions:
				if action.settings["MUTE"] == True:
					self.params["VISIBILITY"] = 0

			time.sleep(0.01)

		print("Goodbye!")

	def __call__(self, event, data=None):
		message, deltatime = event

		print(message)
		vel = message[0]
		key = message[1]
		state = message[2] * 2

		for midiInput in self.inputs:
			if(midiInput.key == key):
				if(midiInput.type == "trigger" and state != 0 ):
					midiInput.trigger(self.params, state)
				if(midiInput.type == "trigger_hold"):
					midiInput.triggerHold(self.params, state)
				if(midiInput.type == "toggle" and state != 0):
					midiInput.toggle(self.params)
				if(midiInput.type == "hold"):
					midiInput.hold(self.params, 255 if state > 0 else 0)
				if(midiInput.type == "knob"):
					midiInput.knob(self.params, state)

App().main()
