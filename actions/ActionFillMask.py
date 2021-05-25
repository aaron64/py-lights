from actions.Action import Action
from actions.Setting import MAX_SPEED_BOUNDS, MAX_POSITION_BOUNDS

from rpi_ws281x import Color
from colors import *
from strip_utils import *
from Timer import Timer

###
# ActionFillMask: Fills the LEDs with a mask from a single point
# Settings:
# 	Intensity - Intensity of the action
# 	Velocity  - Speed and direction of flow
###
class ActionFillMask(Action):
	def __init__(self, params, name=None, mask=None):
		super(ActionFillMask, self).__init__(params, name, "Fill", False, mask)
		self.register_setting("Speed", MAX_SPEED_BOUNDS)
		self.register_setting("Position", MAX_POSITION_BOUNDS)

		self.timer = Timer()
		self.offset = 0

	def update(self, params):
		if self.timer.expired():
			self.timer.reset()
			self.offset += self.get("Speed")

	def set(self, control, val, params):
		super().set(control, val, params)

	def trigger(self, app, params, velocity):
		self.offset = 0

	def render(self, params, strip):
		for x in self.mask:
			distance = abs(x - self.get("Position"))
			if distance < self.offset:
				mask_pixel(strip, x, 1-self.volume())
	
