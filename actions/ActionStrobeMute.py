from actions.Action import Action

class ActionStrobeMute(Action):
	def __init__(self, params):
		super(ActionStrobeMute, self).__init__(params)
		self.settings["Speed"] = 5
		self.settings["On"] = 0

		self.counter = 0
		self.state = True

	def update(self, params):
		self.counter += 1

		if self.counter >= self.settings["Speed"]:
			self.counter = 0
			self.state = not self.state

		if self.state and self.settings["On"] > 127:
			self.settings["MUTE"] = True
		else:
			self.settings["MUTE"] = False
