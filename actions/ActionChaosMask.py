from actions.Action import Action
from rpi_ws281x import Color
from colors import *
from strip_utils import *
from Timer import Timer

import colorsys
import random

###
# ActionChaosMask: Masks a random strobe
# Settings:
# 	Intensity - Intensity of the action
# 	Speed	  - Time it takes for a color to reset
###
class ActionChaosMask(Action):
	def __init__(self, params, mask=None):
		super(ActionChaosMask, self).__init__(params, False, mask)
		self.settings["Speed"] = 50

		self.buffer = []
		for i in range(params['LEDCount']):
			self.buffer.append({
				"timer": Timer(random.randint(self.settings["Speed"], self.settings["Speed"]*2)),
				"on": random.choice([True, False])
			})

	def update(self, params):
		for buff in self.buffer:
			if buff["timer"].expired():
				buff["timer"].duration = random.randint(self.settings["Speed"], self.settings["Speed"]*2)
				buff["timer"].reset()

				buff["on"] = not buff["on"]

	def render(self, params, strip):
		if self.volume() != 0:
			for x in self.mask:
				if self.buffer[x]["on"]:
					maskPixel(strip, x, 1-self.volume())


