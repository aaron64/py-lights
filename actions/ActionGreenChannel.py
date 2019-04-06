from actions.Action import Action

class ActionGreenChannel(Action):
	def __init__(self, params):
		super(ActionGreenChannel, self).__init__(params)
		self.settings["Val"] = 0

	def update(self, params):
		self.settings["G"] = self.settings["Val"]
		
