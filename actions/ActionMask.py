from actions.Action import Action
from strip_utils import *

###
# ActionMask: Mutes the LEDs when on
# Settings:
# 	Intensity - Sets intensity of the mask
###
class ActionMask(Action):
	def __init__(self, params, name=None, mask=None):
		super(ActionMask, self).__init__(params, name, "Mask", False, mask)

	def update(self, params):
		pass

	def render_mask(self, params, strip):
		if self.volume() != 0:
			for x in self.mask:
				maskPixel(strip, x, 1-self.volume())
