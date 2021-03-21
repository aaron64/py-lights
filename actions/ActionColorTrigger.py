from actions.Action import Action
from Color import Color

###
# ActionColorTrigger: displays a color on key press
# Settings:
# 	Attack(0) - Time of the actions attack
#	Sustain(20) - Time of the actions sustain
#	Release(0) - Time of the actions release
###
class ActionColorTrigger(Action):
	def __init__(self, params, color = Color.white()):
		super(ActionColorTrigger, self).__init__(params)
		
		self.triggerTime = 0
		self.color = color
		self.val = 0

	def trigger(self, params, val):
		self.triggerTime = params["Counter"]
		self.val = val

	def update(self, val, control, params, strip):
		if self.triggerTime != 0:

			intensity = 0
			timeLapsed = params["Counter"] - self.triggerTime
			if timeLapsed < self.settings["Attack"]:
				intensity = int((float(timeLapsed)/(self.settings["Attack"]+1)) * self.val)
			elif timeLapsed < self.settings["Attack"] + self.settings["Sustain"]:
				intensity = self.val
			elif timeLapsed < self.settings["Attack"] + self.settings["Sustain"] + self.settings["Release"]:
				time_till_release = self.settings["Attack"] + self.settings["Sustain"]
				intensity = self.val - int((float(timeLapsed - time_till_release)/(self.settings["Release"]+1)) * self.val)
			else:
				self.triggerTime = 0

			self.settings["Color"].r = int(self.color.r * (float(intensity)/255))
			self.settings["Color"].g = int(self.color.g * (float(intensity)/255))
			self.settings["Color"].b = int(self.color.b * (float(intensity)/255))
