from actions.Action import Action
from actions.Setting import MAX_SPEED_BOUNDS

from rpi_ws281x import Color
from colors import *
from strip_utils import *
from Timer import Timer

###
# ActionStrobe: Displays a color in a strobe pattern
# Settings:
# 	Intensity - Intensity of the action
#	Speed	  - Timeing of the strobe effect
###
class ActionStrobe(Action):
	def __init__(self, params, name=None, color = WHITE, mask=None):
		super(ActionStrobe, self).__init__(params, name, "Strobe", False, mask)
		self.register_setting("Speed", MAX_SPEED_BOUNDS)
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
		if self.on and self.volume() != 0:
			for x in self.mask:
				addColorToStrip(strip, x, level_color(self.color, self.get("Volume") * self.volume()))