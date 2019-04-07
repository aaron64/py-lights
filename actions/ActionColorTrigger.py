from actions.Action import Action
from Color import Color

class ActionColorTrigger(Action):
	def __init__(self, params, color = Color.white()):
		super(ActionColorTrigger, self).__init__(params)
		self.settings["Attack"] = 0
		self.settings["Sustain"] = 0
		self.settings["Release"] = 20
		self.triggerTime = 0
                self.color = color

	def trigger(self, params, val):
		self.triggerTime = params["Counter"]

	def update(self, params):
		if self.triggerTime != 0:

			intensity = 0
			timeLapsed = params["Counter"] - self.triggerTime
			if timeLapsed < self.settings["Attack"]:
				intensity = int((float(timeLapsed)/(self.settings["Attack"])) * 255)
			elif timeLapsed < self.settings["Attack"] + self.settings["Sustain"]:
				intensity = 255
			elif timeLapsed < self.settings["Attack"] + self.settings["Sustain"] + self.settings["Release"]:
                                time_till_release = self.settings["Attack"] + self.settings["Sustain"]
				intensity = 255 - int((float(timeLapsed - time_till_release)/(self.settings["Release"])) * 255)
                        else:
				self.triggerTime = 0

			self.settings["Color"].r = int(self.color.r * float(intensity)/255)
			self.settings["Color"].g = int(self.color.g * float(intensity)/255)
			self.settings["Color"].b = int(self.color.b * float(intensity)/255)
