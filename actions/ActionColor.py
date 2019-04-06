from actions.Action import Action

class ActionRedChannel(Action):
	def __init__(self, params, color = Color.WHITE):
		super(ActionRedChannel, self).__init__(params)
		self.settings["Val"] = 0
		self.color = color

	def update(self, params):
		self.settings["Color"].r = self.color.r * (self.settings["Val"]/255)
		self.settings["Color"].g = self.color.g * (self.settings["Val"]/255)
		self.settings["Color"].b = self.color.b * (self.settings["Val"]/255)
	
		
