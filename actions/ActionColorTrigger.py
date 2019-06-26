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
	def __init__(self, params, color = Color.white(), attack=0, sustain=20, release=0):
		super(ActionColorTrigger, self).__init__(params, "Color Trigger")
		self.settings["Attack"] = attack
		self.settings["Sustain"] = sustain
		self.settings["Release"] = release
		self.parameters["Color"] = color
		
		self.triggerTime = 0
		self.val = 0

	def trigger(self, params, _input, val):
		self.triggerTime = params["Counter"]
		self.val = val

	def update(self, params):
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

			self.outputColor.r = int(self.parameters["Color"].r * (float(intensity)/255))
			self.outputColor.g = int(self.parameters["Color"].g * (float(intensity)/255))
			self.outputColor.b = int(self.parameters["Color"].b * (float(intensity)/255))
