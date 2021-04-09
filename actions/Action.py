from rpi_ws281x import Color

class Action(object):
	def __init__(self, params, inverse=False, mask=None):
		self.inverse = inverse
		self.settings = {
			"Intensity": 0,
			"Volume": 1
		}

		if mask == None:
			self.mask = [*range(params["LEDCount"])]
		elif isinstance(mask, str):
			self.mask = []
			for i in range(params["LEDCount"]):
				if eval(mask, {"x": i}):
					self.mask.append(i)
		else:
			self.mask = mask

	def set(self, control, val, params):
		try:
			self.settings[control] = val
		except Exception as e:
			print(e)

	def volume(self):
		return self.settings["Intensity"] * self.settings["Volume"]

	def is_on(self):
		return self.settings["Intensity"] > 0

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
