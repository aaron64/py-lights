from actions.Action import Action
from actions.Setting import MAX_VELOCITY_BOUNDS

from rpi_ws281x import Color
from colors import *
from strip_utils import *
from Timer import Timer

from math import sin, pi

###
# ActionNoise: Displays 1D perlin noise
# Settings:
# 	Intensity - Intensity of the action
###
class ActionNoise(Action):
	def __init__(self, params, name=None, color = WHITE, mask=None):
		super(ActionNoise, self).__init__(params, name, "Noise", False, mask)
		self.register_setting("Velocity", MAX_VELOCITY_BOUNDS)

		self.timer = Timer(60)
		self.offset = 0

		self.color = color

	def update(self, params):
		if self.timer.expired():
			self.timer.reset()
			self.offset += self.get("Velocity")

	def render(self, params, strip):
		if self.volume() != 0:
			for x in self.mask:
				pos = x + self.offset
				width = 0.2
				val = sin(width * pos) + sin(pi * pos)+1
				val *= 0.5
				addColorToStrip(strip, x, level_color(self.color, val * self.volume()))
	
