from actions.Action import Action
from actions.Setting import MAX_SPEED_BOUNDS, MAX_POSITION_BOUNDS

from rpi_ws281x import Color
from colors import *
from strip_utils import *
from Timer import Timer

###
# ActionFill: Fills the LEDs from a single point
# Settings:
# 	Intensity - Intensity of the action
# 	Velocity  - Speed and direction of flow
###
class ActionFill(Action):
	def __init__(self, params, name=None, color = WHITE, mask=None):
		super(ActionFill, self).__init__(params, name, "Fill", False, mask)
		self.register_setting("Speed", MAX_SPEED_BOUNDS)
		self.register_setting("Position", MAX_POSITION_BOUNDS)

		self.timer = Timer(60)
		self.offset = 0

		self.color = color

	def update(self, params):
		if self.timer.expired():
			self.timer.reset()
			self.offset += self.get("Speed")

	def set(self, control, val, params):
		super().set(control, val, params)

	def trigger(self, params, velocity):
		self.offset = 0

	def render(self, params, strip):
		if self.volume() != 0:
			for x in self.mask:
				distance = abs(x - self.get("Position"))
				if distance < self.offset:
					addColorToStrip(strip, x, level_color(self.color, self.volume()))
	
