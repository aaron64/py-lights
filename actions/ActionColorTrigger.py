from actions.Action import Action

class ActionGreenChannel(Action):
	def __init__(self, params):
		super(ActionGreenChannel, self).__init__(params)
		self.settings["Attack"] = 0
		self.settings["Sustain"] = 0
		self.settings["Release"] = 0

	def update(self, params):
		self.settings["G"] = self.settings["Val"]
		
