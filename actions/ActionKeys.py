from actions.Action import Action
from Color import Color

###
# ActionKeys: Displays a trigger for a range of keys
# Low - Low of key range
# High - High of key range
# Settings:
# 	Attack(0) - Time of the actions attack
#	Release(0) - Time of the actions release
###
class ActionKeys(Action):
	def __init__(self, params, low, high, col1=Color.white(), col2=Color.white(), attack=0, release=0):
		super(ActionKeys, self).__init__(params, "Keys")
		self.settings["Attack"] = attack
		self.settings["Release"] = release

		self.parameters["Color1"] = col1
		self.parameters["Color2"] = col2
		self.currentColor = col1

		self.triggerTime = 0
		self.val = 0
		self.state = "off"

		self.low = low
		self.high = high

		for i in range(low, high):
			triggerName = "Trigger " + str(i)
			self.settings[triggerName] = 0

			color = Color.interpolate(col1, col2, (float(i-low)/(high-low)))
			app.addInput(self, "trigger_hold", i, triggerName)
		
	def trigger(self, params, _input, val):
		self.triggerTime = params["Counter"]
		self.val = val
		self.state = "attack"

		self.currentColor = Color.interpolate(col1, col2, (float(_input.key-low)/(high-low)))

	def release(self, _input, params):
		self.triggerTime = params["Counter"]
		self.state = "release"

	def update(self, params):
		if self.triggerTime != 0:

			intensity = 0
			timeLapsed = params["Counter"] - self.triggerTime
			if self.state == "attack":
				intensity = int((float(timeLapsed)/(self.settings["Attack"]+1)) * self.val)
				if timeLapsed >= self.settings["Attack"]:
					self.state = "sustain"
			elif self.state == "sustain":
				intensity = self.val
			elif self.state == "release":
				intensity = self.val - int((float(timeLapsed)/(self.settings["Release"]+1)) * self.val)
				if timeLapsed >= self.settings["Release"]:
					self.state = "off"
			else:
				self.triggerTime = 0

			self.outputColor.r = int(self.currentColor.r * (float(intensity)/255))
			self.outputColor.g = int(self.currentColor.g * (float(intensity)/255))
			self.outputColor.b = int(self.currentColor.b * (float(intensity)/255))
		
