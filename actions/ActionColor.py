from actions.Action import Action

class ActionRedChannel(Action):
	def __init__(self, params, color = Color.WHITE):
		super(ActionRedChannel, self).__init__(params)
		self.settings["Val"] = 0
		self.color = color

	def update(self, params):
		self.settings["Color"].r = int(self.color.r * float(self.settings["Val"]/255))
		self.settings["Color"].g = int(self.color.g * float(self.settings["Val"]/255))
		self.settings["Color"].b = int(self.color.b * float(self.settings["Val"]/255))
	
		
