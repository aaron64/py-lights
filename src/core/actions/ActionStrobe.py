from core.actions.Action import Action
from core.actions.Setting import MAX_STROBE_BOUNDS

from rpi_ws281x import Color
from core.colors import *
from core.utils.strip_utils import *
from core.utils.Timer import Timer

###
# ActionStrobe: Displays a color in a strobe pattern
# Settings:
# 	Intensity - Intensity of the action
#	Speed	  - Timeing of the strobe effect
###
class ActionStrobe(Action):
	def __init__(self, params, name=None, color = WHITE, mask=None):
		super(ActionStrobe, self).__init__(params, name, "Strobe", False, mask)
		self.register_setting("Speed", MAX_STROBE_BOUNDS)
		self.on = False
		self.color = color
		self.timer = Timer(self.get("Speed"))

	def update(self, params):
		if self.timer.expired():
			self.timer.reset()
			self.on = not self.on

	def set(self, control, val, params):
		super().set(control, val, params)
		if control == "Speed":
			self.timer.duration = self.get("Speed")
			self.timer.soft_reset()

	def render(self, params, strip):
		if self.on:
			for x in self.mask:
				add_color_to_strip(strip, x, level_color(self.color, self.volume()))