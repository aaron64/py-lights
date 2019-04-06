from actions.Action import Action

class ActionGreenChannel(Action):
	def __init__(self, params):
		super(ActionGreenChannel, self).__init__(params)
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
				intensity = (timeLapsed/self.settings["Attack"]) * 255
			else if timeLapsed < self.settings["Sustain"]:
				intensity = 255
			else if timeLapsed < self.settings["Release"]:
				intensity = 255 - (timeLapsed/self.settings["Attack"]) * 255
			else
				self.triggerTime = 0

			self.settings["R"] = intensity
			self.settings["G"] = intensity
			self.settings["B"] = intensity