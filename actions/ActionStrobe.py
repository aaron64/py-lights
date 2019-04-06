from actions.Action import Action

class ActionStrobe(Action):
	def __init__(self, params):
		super(ActionStrobe, self).__init__(params)
		self.settings["Intensity"] = 0
		self.settings["Speed"] = 5

		self.counter = 0
		self.state = True

	def update(self, params):
		self.counter += 1

		if self.counter >= self.settings["Speed"]:
			self.counter = 0
			self.state = not self.state

		out = 0
		if (params["Counter"]/(self.settings["Speed"]+1))%2 == 1:
			out = self.settings["Intensity"]
		
		self.settings["R"] = out
		self.settings["G"] = out
		self.settings["B"] = out
