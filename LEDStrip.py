
def clear_LEDs(LEDs):
	for LED in LEDs:
		LED.R = 0
		LED.G = 0
		LED.B = 0
		LED.A = 1