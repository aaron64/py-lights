from actions.Action import Action

class ActionRedChannel(Action):
	def __init__(self, params):
		super(ActionRedChannel, self).__init__(params)
		self.settings["Val"] = 0

	def update(self, params):
		self.settings["R"] = self.settings["Val"]
	
		
