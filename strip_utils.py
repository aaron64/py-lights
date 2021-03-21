from colors import *

def addColorToStrip(strip, index, color):
	strip.setPixelColor(index, add_colors(strip.getPixelColor(index), color))
