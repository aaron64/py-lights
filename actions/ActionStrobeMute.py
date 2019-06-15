from actions.Action import Action

###
# ActionMuteStrobe: Mutes the LEDs in a strobe pattern
# Settings:
# 	Mute(0) - Mutes the LEDs if value > 127
#	Speed(5) - Timeing of the strobe effect
###
class ActionStrobeMute(Action):
	def __init__(self, params):
		super(ActionStrobeMute, self).__init__(params, "Strobe Mute")
		self.settings["Speed"] = 5
		self.settings["On"] = 0

	def update(self, params):
		mute = False
		if (params["Counter"]/(self.settings["Speed"]+1))%2 == 1:
			mute = True

		if mute and self.settings["On"] > 127:
			self.mute = True
		else:
			self.mute = False
