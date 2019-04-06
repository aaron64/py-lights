from Color import Color

class Action(object):
	def __init__(self, params, inverse=False):
		self.inverse = inverse
		self.settings = {
			"Color": Color(0,0,0),
			"MUTE": False
		};

	def getR(self):
		return self.settings["R"]

	def getG(self):
		return self.settings["G"]

	def getB(self):
		return self.settings["B"]

	def updateSetting(self, setting, val):
		self.settings[setting] = val

	def update(self, params):
		pass

        def trigger(self, params, val):
		pass
