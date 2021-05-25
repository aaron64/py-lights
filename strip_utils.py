from colors import *

def add_color_to_strip(strip, index, color):
	strip.setPixelColor(index, add_colors(strip.getPixelColor(index), color))

def set_color(strip, index, color):
	strip.setPixelColor(index, color)

def mask_pixel(strip, index, intensity):
	color = strip.getPixelColor(index)
	strip.setPixelColor(index, level_color(color, intensity))

def clear_LEDs(strip, leds):
	for i in range(0, leds):
		strip.setPixelColor(i, Color(0, 0, 0))