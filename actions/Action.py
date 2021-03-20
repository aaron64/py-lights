from Color import Color

###
# Action
# Settings:
#	Color(Color(0,0,0)) - Output color of the action
#	MUTE(False) - Whether to mute LEDs
###
class Action(object):
	def __init__(self, params, inverse=False):
		self.inverse = inverse
		self.settings = {
			"Color": Color(0,0,0),
			"MUTE": False
		};

	def updateSetting(self, setting, val):
		self.settings[setting] = val

	def update(self, params):
		pass

	def trigger(self, params, val):
		pass

	def release(self, params):
		pass
