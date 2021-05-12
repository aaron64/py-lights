from actions.Action import Action
from actions.Setting import MAX_VELOCITY_BOUNDS

from rpi_ws281x import Color
from colors import *
from strip_utils import *
from Timer import Timer

import random
import colorsys

###
# ActionRainbow: Displays a HSV rainbow over the entire strip
# Settings:
# 	Intensity - Intensity of the rainbow
# 	Speed	  - Speed of rainbow movement
###
class ActionRainbow(Action):
	def __init__(self, params, name=None, mask=None):
		super(ActionRainbow, self).__init__(params, name, "Rainbow", False, mask)
		self.register_setting("Velocity", MAX_VELOCITY_BOUNDS)

		self.timer = Timer()
		self.offset = 1

	def update(self, params):
		if self.timer.expired():
			self.timer.reset()
			self.offset += self.get("Velocity")
			# if self.offset == params["LEDCount"]:
			# 	self.offset = 0

	def set(self, control, val, params):
		super().set(control, val, params)
		# if control == "Speed":
			# self.timer = Timer(self.settings["Speed"])


	def render(self, params, strip):
		count = params["LEDCount"]
		if self.volume() != 0:
			for x in self.mask:
				(r, g, b) = colorsys.hsv_to_rgb((x+self.offset)/count, 1.0, 1.0)
				color = Color(int(255 * r), int(255 * g), int(255 * b))

				add_color_to_strip(strip, x, level_color(color, self.volume()))


