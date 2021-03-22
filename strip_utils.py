from colors import *

def addColorToStrip(strip, index, color):
	strip.setPixelColor(index, add_colors(strip.getPixelColor(index), color))

def maskPixel(strip, index, intensity):
	color = strip.getPixelColor(index)
	strip.setPixelColor(index, level_color(color, intensity))