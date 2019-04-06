from actions.Action import Action

class ActionColorTrigger(Action):
	def __init__(self, params, color = Color.WHITE):
		super(ActionColorTrigger, self).__init__(params)
		self.settings["Color"] = color
		self.settings["Attack"] = 10
		self.settings["Sustain"] = 15
		self.settings["Release"] = 20
		self.triggerTime = 0

	def trigger(self, params, val):
		self.triggerTime = params["Counter"]

	def update(self, params):
		if self.triggerTime != 0:

			intensity = 0
			timeLapsed = params["Counter"] - self.triggerTime
			if timeLapsed < self.settings["Attack"]:
				intensity = int((float(timeLapsed)/(self.settings["Attack"])) * 255)
			elif timeLapsed < self.settings["Sustain"]:
				intensity = 255
			elif timeLapsed < self.settings["Release"]:
				intensity = int((float(timeLapsed)/(self.settings["Attack"])) * 255)
                        else:
				self.triggerTime = 0

			self.settings["R"] = intensity
			self.settings["G"] = intensity
			self.settings["B"] = intensity
