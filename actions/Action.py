from rpi_ws281x import Color
from actions.Setting import Setting

class Action(object):
	def __init__(self, params, name, type, inverse=False, mask=None):
		self.inverse = inverse
		self.settings = {}

		self.register_setting("Intensity")
		self.register_setting("Volume")

		self.set("Volume", 1, params)

		if name is None:
			name = "New %s" % type
		self.name = name

		self.type = type

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
			self.settings[control].value = val
		except Exception as e:
			print(e)

	def get(self, name):
		return self.settings[name].value

	def volume(self):
		return self.get("Intensity") * self.get("Volume")

	def is_on(self):
		return self.get("Intensity") > 0

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

	def register_setting(self, name, bounds=None):
		setting = Setting(name, bounds)
		self.settings[name] = setting

	def to_dict(self):
		return {
			"name": self.name,
			"type": self.type,
			"settings": list(map(Setting.to_dict, self.settings.values()))
		}