from actions.Action import Action
from actions.Setting import MAX_STROBE_BOUNDS

from rpi_ws281x import Color
from colors import *
from strip_utils import *
from Timer import Timer

import colorsys
import random

###
# ActionChaos: Displays a strobe of random colors at random times
# Settings:
# 	Intensity - Intensity of the action
# 	Speed	  - Time it takes for a color to reset
###
class ActionChaos(Action):
	def __init__(self, params, name=None, colors = None, mask=None):
		super(ActionChaos, self).__init__(params, name, "Chaos", False, mask)
		self.register_setting("Speed", MAX_STROBE_BOUNDS)
		self.colors = colors

		self.buffer = []
		for i in range(params['LEDCount']):
			self.buffer.append({
				"timer": Timer(random.randint(round(self.get("Speed")), round(self.get("Speed")*2))),
				"color": self._get_next_color()
			})

	def _get_next_color(self):
		if self.colors is None:
			x = random.uniform(0, 1)
			(r, g, b) = colorsys.hsv_to_rgb(x, 1.0, 1.0)
			color = Color(int(255 * r), int(255 * g), int(255 * b))
			return color
		else:
			return random.choice(self.colors)

	def set(self, control, val, params):
		super().set(control, val, params)
		if control == "Speed":
			for i in range(params['LEDCount']):
				self.buffer[i]["timer"].soft_reset()

	def update(self, params):
		for buff in self.buffer:
			if buff["timer"].expired():
				buff["timer"].duration = random.randint(round(self.get("Speed")), round(self.get("Speed")*2))
				buff["timer"].reset()

				x = random.uniform(0, 1)
				(r, g, b) = colorsys.hsv_to_rgb(x, 1.0, 1.0)
				color = Color(int(255 * r), int(255 * g), int(255 * b))
				buff["color"] = self._get_next_color()

	def render(self, params, strip):
		for x in self.mask:
			add_color_to_strip(strip, x, level_color(self.buffer[x]["color"], self.volume()))


