
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 255, 255)


class Color:
	def __init__(self, r, g, b):
		self.r = min(r, 255)
		self.g = min(g, 255)
		self.b = min(b, 255)

	