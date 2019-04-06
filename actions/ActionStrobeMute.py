from actions.Action import Action

class ActionStrobe(Action):
	def __init__(self, params):
		super(ActionStrobe, self).__init__(params)
		self.settings["Speed"] = 5
		self.settings["On"] = 0

		self.counter = 0
		self.state = True

	def update(self, params):
		counter++

		if counter >= self.settings["Speed"]:
			counter = 0
			self.state = !self.state

		if self.state and self.settings["On"] > 127:
			self.settings["MUTE"] = True
		else:
			self.settings["MUTE"] = False
