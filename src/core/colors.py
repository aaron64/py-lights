import random
from rpi_ws281x import Color

WHITE   = Color(255, 255, 255)
BLACK	= Color(0, 0, 0)

RED     = Color(255, 0, 0)
GREEN   = Color(0, 255, 0)
BLUE    = Color(0, 0, 255)

CYAN    = Color(0, 255, 255)
MAGENTA = Color(255, 0, 255)
YELLOW  = Color(255, 255, 0)

def get_random_color():
	return random.choice([CYAN, MAGENTA, YELLOW, RED, GREEN, BLUE, WHITE, BLACK])

def level_color(col, level):
	return Color(
		(int)(red(col) * level),
		(int)(green(col) * level),
		(int)(blue(col) * level)
	)

def interpolate_colors(col1, col2, val):
	return Color(
		red(col1),
		green(col1),
		blue(col1)
	)

def add_colors(col1, col2):
	r = (red(col1) + red(col2))
	g = (green(col1) + green(col2))
	b = (blue(col1) + blue(col2))

	r = 255 if r > 255 else r
	g = 255 if g > 255 else g
	b = 255 if b > 255 else b
	return Color(r, g, b)

def red(col):
	return ((255 << 16) & col) >> 16 

def green(col):
	return ((255 << 8) & col) >> 8 

def blue(col):
	return ((255 << 0) & col) >> 0 