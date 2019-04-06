from actions.Action import Action

class ActionStrobe(Action):
	def __init__(self, params):
		super(ActionStrobe, self).__init__(params)
		self.settings["Intensity"] = 0
		self.settings["Speed"] = 5

		self.counter = 0
		self.state = True

	def update(self, params):
		counter++

		if counter >= self.settings["Speed"]:
			counter = 0
			self.state = !self.state

		out = 0
		if self.state:
			out = self.settings["Intensity"]
		
		self.settings["R"] = out
		self.settings["G"] = out
		self.settings["B"] = out