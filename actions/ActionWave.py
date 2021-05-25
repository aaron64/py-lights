from actions.Action import Action
from actions.Setting import MAX_VELOCITY_BOUNDS, MAX_WIDTH_BOUNDS

from rpi_ws281x import Color
from colors import *
from strip_utils import *
from Timer import Timer

from math import sin, pi

###
# ActionWave: Displays a color
# Settings:
# 	Intensity - Intensity of the action
###
class ActionWave(Action):
	def __init__(self, params, name=None, color=WHITE, mask=None):
		super(ActionWave, self).__init__(params, name, "Color", False, mask)
		self.register_setting("Velocity", MAX_VELOCITY_BOUNDS)
		self.register_setting("Width", MAX_WIDTH_BOUNDS)

		self.set(params, "Velocity", 0)
		self.set(params, "Width", 0.2)

		self.timer = Timer()
		self.offset = 0

		self.color = color

	def update(self, params):
		if self.timer.expired():
			self.timer.reset()
			self.offset += self.get("Velocity")

	def render(self, params, strip):
		for x in self.mask:
			level = (sin((x+self.offset)/self.get("Width"))+1)/2
			add_color_to_strip(strip, x, level_color(self.color, level * self.volume()))
	
