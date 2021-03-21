from actions.Action import Action
from Color import Color

###
# ActionColorTriggerHold: displays a color on key held (similar to ActionColorTrigger with infinite sustain)
# Settings:
# 	Attack(0) - Time of the actions attack
#	Release(0) - Time of the actions release
###
class ActionColorTriggerHold(Action):
	def __init__(self, params, color = Color.white(), attack=0, release=0):
		super(ActionColorTriggerHold, self).__init__(params)
		self.settings["Attack"] = attack
		self.settings["Release"] = release
		self.triggerTime = 0
		self.color = color
		self.val = 0
		self.state = "off"

	def trigger(self, params, val):
			self.triggerTime = params["Counter"]
			self.val = val
			self.state = "attack"

	def release(self, params):
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

			self.settings["Color"].r = int(self.color.r * (float(intensity)/255))
			self.settings["Color"].g = int(self.color.g * (float(intensity)/255))
			self.settings["Color"].b = int(self.color.b * (float(intensity)/255))
