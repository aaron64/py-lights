from actions.Action import Action


###
# ActionStrobeTap: Displays a color in a strobe pattern to the beat of a tap
# Settings:
# 	Intensity(0) - Intensity of the action
###
class ActionStrobeTap(Action):
	def __init__(self, params, color = Color.white()):
		super(ActionStrobeTap, self).__init__(params)
		self.settings["Intensity"] = 0
		self.taps = 0
		self.rate = 0
		self.taps = 0
		self.countAtTap = 0
		self.color = color

	def update(self, params):
		out = 0
		if (params["Counter"]/(self.rate+1))%2 == 1:
			out = self.settings["Intensity"]
		
		# self.settings["Color"].r = int(self.color.r * (float(out)/255))
		# self.settings["Color"].g = int(self.color.g * (float(out)/255))
		# self.settings["Color"].b = int(self.color.b * (float(out)/255))

	def trigger(self, params, val):
		self.taps += 1
		if self.taps%2 == 0:
			self.rate = params["Counter"] - self.countAtTap
		else:
			self.countAtTap = params["Counter"]
