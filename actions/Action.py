from Color import Color

###
# Action
###
class Action(object):
	def __init__(self, params, name, inverse=False):
		self.inverse = inverse
		self.name = name
		self.settings = {}
		self.parameters = {}

		self.outputColor = Color(0,0,0)
		self.mute = False
		self.inputs = []

	def __unicode__(self):
		return u"" + self.name

	def getR(self):
		return self.settings["R"]

	def getG(self):
		return self.settings["G"]

	def getB(self):
		return self.settings["B"]

	def updateSetting(self, setting, val):
		self.settings[setting] = val

	def getSetting(self, setting):
		return self.settings[setting]

	def update(self, params):
		pass

	def trigger(self, params, _input, val):
		pass

	def release(self, params, _input):
		pass

	def addInput(self, _input):
		self.inputs.append(_input)

	def getHeaderCSS(self):
		if not ("Color" in self.parameters):
			return ""
		print(self.parameters["Color"])
		print(str(self.parameters["Color"]))
		return "background-image: linear-gradient(to right, rgba(0,0,0,0), rgba(0,0,0,0), rgb(" + str(self.parameters["Color"]) + "))"