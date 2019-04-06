
class Action(object):
	def __init__(self, params, inverse=False):
		self.inverse = inverse
		self.settings = {
			"R": 0,
			"G": 0,
			"B": 0
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
