from rpi_ws281x import Color

###
# Action
# Settings:
#	Color(Color(0,0,0)) - Output color of the action
#	MUTE(False) - Whether to mute LEDs
###
class Action(object):
	def __init__(self, params, inverse=False, mask="ALL"):
		self.inverse = inverse
		self.settings = {
			"Color": Color(0,0,0),
			"MUTE": False
		};
		print(params['LEDCount'])

		if mask == "ALL":
			self.mask = [*range(params["LEDCount"])]
		elif isinstance(mask, str):
			self.mask = []
			for i in range(params["LEDCount"]):
				if eval(mask, {"x": i}):
					self.mask.append(i)
		else:
			self.mask = mask

	def set(self, control, val, params):
		self.settings[control] = val

	def update(self, params):
		pass

	def render(self, params, strip):
		pass

	def render_mask(self, params, strip):
		pass

	def trigger(self, params, val):
		pass

	def release(self, params):
		pass
