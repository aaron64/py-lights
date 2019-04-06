from actions.Action import Action

class ActionBlueChannel(Action):
	def __init__(self, params):
		super(ActionBlueChannel, self).__init__(params)
		self.settings["Val"] = 0

	def update(self, params):
		self.settings["B"] = self.settings["Val"]

	
		
