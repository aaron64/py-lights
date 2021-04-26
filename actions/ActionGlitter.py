from actions.Action import Action
from actions.Setting import MAX_SPEED_BOUNDS

from rpi_ws281x import Color
from colors import *
from strip_utils import *
from Timer import Timer

from math import sin, pi
import random

###
# ActionGlitter: Displays a randomly timed soft strobe
# Settings:
# 	Intensity(0) - Intensity of the action
# 	Speed		 - Minimum speed of for an LED to complete a cycle
###
class ActionGlitter(Action):
	def __init__(self, params, name=None, color=WHITE, mask=None):
		super(ActionGlitter, self).__init__(params, name, "Glitter", False, mask)
		self.register_setting("Speed", MAX_SPEED_BOUNDS)

		self.color = color

		self.buffer = []
		for i in range(params['LEDCount']):
			self.buffer.append({
				"timer": Timer(random.randint(self.get("Speed"), self.get("Speed")*2)),
				"color": get_random_color()
			})

	def update(self, params):
		for buff in self.buffer:
			if buff["timer"].expired():
				buff["timer"].duration = random.random() * self.get("Speed") + self.get("Speed")
				buff["timer"].reset()
				if buff["color"] == self.color:
					buff["color"] = BLACK
				else:
					buff["color"] = self.color

	def render(self, params, strip):
		if self.volume() != 0:
			for x in self.mask:
				pct_finished = self.buffer[x]["timer"].percent_finished()
				velocity = sin(pct_finished*pi*2)*0.5 + 0.5
				if self.buffer[x]["color"] != BLACK:
					addColorToStrip(strip, x, level_color(self.buffer[x]["color"], velocity * self.volume()))


