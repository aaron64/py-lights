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
	r1 = red(col1)
	r2 = red(col2)
	g1 = green(col1)
	g2 = green(col2)
	b1 = blue(col1)
	b2 = blue(col2)

	r = min(255, r1 + r2)
	g = min(255, g1 + g2)
	b = min(255, b1 + b2)

	return Color(r, g, b)

def red(col):
	return ((255 << 16) & col) >> 16 

def green(col):
	return ((255 << 8) & col) >> 8 

def blue(col):
	return ((255 << 0) & col) >> 0 