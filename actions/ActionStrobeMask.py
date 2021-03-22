from actions.Action import Action
from strip_utils import *

###
# ActionMuteStrobe: Mutes the LEDs in a strobe pattern
# Settings:
# 	Mute(0) - Mutes the LEDs if value > 127
#	Speed(5) - Timeing of the strobe effect
###
class ActionStrobeMask(Action):
	def __init__(self, params, mask="ALL"):
		super(ActionStrobeMask, self).__init__(params, False, mask)
		self.settings["Intensity"] = 0
		self.settings["Speed"] = 3
		self.on = False
		self.nextFlip = params['Counter'] + self.settings["Speed"]

	def update(self, params):
		if params['Counter'] > self.nextFlip:
			self.nextFlip = params['Counter'] + self.settings["Speed"]		
			self.on = not self.on

	def render_mask(self, params, strip):
		if self.on and self.settings["Intensity"] != 0:
			for x in self.mask:
				maskPixel(strip, x, 1-self.settings["Intensity"])
