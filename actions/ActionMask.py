from actions.Action import Action
from strip_utils import *

###
# ActionMask: Mutes the LEDs when on
# Settings:
# 	Mute(0) - Mutes the LEDs if value > 127
###
class ActionMask(Action):
	def __init__(self, params, mask="ALL"):
		super(ActionMask, self).__init__(params, False, mask)
		self.settings["Intensity"] = 0

	def update(self, params):
		pass

	def render_mask(self, params, strip):
		if self.settings["Intensity"] != 0:
			for x in self.mask:
				maskPixel(strip, x, 1-self.settings["Intensity"])
