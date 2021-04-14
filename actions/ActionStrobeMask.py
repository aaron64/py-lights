from actions.Action import Action
from actions.Setting import MAX_SPEED_BOUNDS

from strip_utils import *
from Timer import Timer

###
# ActionMuteStrobe: Mutes the LEDs in a strobe pattern
# Settings:
# 	Mute  - Mutes the LEDs if value > 127
#	Speed - Timeing of the strobe effect
###
class ActionStrobeMask(Action):
	def __init__(self, params, name=None, mask=None):
		super(ActionStrobeMask, self).__init__(params, name, "Strobe Mask", False, mask)
		self.register_setting("Speed", MAX_SPEED_BOUNDS)
		self.on = False
		self.timer = Timer(self.get("Speed"))

	def update(self, params):
		if self.timer.expired():
			self.timer.reset()
			self.on = not self.on

	def set(self, control, val, params):
		super().set(control, val, params)
		if control == "Speed":
			self.timer = Timer(self.get("Speed"))

	def render_mask(self, params, strip):
		if self.on and self.volume() != 0:
			for x in self.mask:
				maskPixel(strip, x, 1-self.volume())
