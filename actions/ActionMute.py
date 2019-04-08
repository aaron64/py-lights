from actions.Action import Action

###
# ActionMute: Mutes the LEDs when on
# Settings:
# 	Mute(0) - Mutes the LEDs if value > 127
###
class ActionMute(Action):
	def __init__(self, params):
		super(ActionMute, self).__init__(params)
		self.settings["On"] = 0

	def update(self, params):
		if self.settings["On"] > 127:
			self.settings["MUTE"] = True
		else:
			self.settings["MUTE"] = False
