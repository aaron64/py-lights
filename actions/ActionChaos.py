from actions.Action import Action
from rpi_ws281x import Color
from colors import *
from strip_utils import *

import random

###
# ActionChaos: Displays a strobe of random colors at random times
# Settings:
# 	Intensity(0) - Intensity of the action
###
class ActionChaos(Action):
	def __init__(self, params, mask="ALL"):
		super(ActionChaos, self).__init__(params, False, mask)
		self.settings["Intensity"] = 0
		self.settings["Speed"] = 1

		self.buffer = []
		for i in range(params['LEDCount']):
			self.buffer.append({
				"life": random.randint(1,20),
				"color": get_random_color()
			})

	def update(self, params):
		for buff in self.buffer:
			buff["life"] -= 1
			if buff["life"] <= 0:
				buff["life"] = random.randint(1,20)
				buff["color"] = get_random_color()

	def render(self, params, strip):
		if self.settings["Intensity"] != 0:
			for x in self.mask:
				addColorToStrip(strip, x, level_color(self.buffer[x]["color"], self.settings["Intensity"]))


