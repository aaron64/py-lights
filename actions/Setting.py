
MAX_SPEED_BOUNDS = (1, 50000)
MAX_POSITION_BOUNDS = (-1024, 1024)
MAX_VELOCITY_BOUNDS = (-1024, 1024)
MAX_STROBE_BOUNDS = (1, 5000)
MAX_WIDTH_BOUNDS = (0.01, 10)

DEFAULT_BOUNDS = (0, 1)

class Setting(object):
	def __init__(self, name, bounds=None):
		self.name = name

		if bounds is None:
			bounds = DEFAULT_BOUNDS
		self.bounds = bounds

		self.value = bounds[0]

	def to_dict(self):
		return {
			"name": self.name,
			"bounds": self.bounds,
			"value": self.value
		}