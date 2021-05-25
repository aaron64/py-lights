
from colors import *

# A factory class for creating actions and inputs
class ActionBuilder():

	###
	# build_keys - creates a range of TriggerHoldKeys that spans between 2 colors
	# low - low key value
	# high - high key value
	# col1 - first color
	# col2 - second color
	###
	@staticmethod
	def build_keys(app, low, high, col1=WHITE, col2=WHITE, attack=0, release=0):
		high += 1
		for i in range(low, high):
			color = interpolate_colors(col1, col2, (float(i-low)/(high-low)))
			# action = app.addAction(ActionColorTriggerHold(app.params, color, attack=attack, release=release))
			# app.add_trigger(action, "trigger_hold", i, "")
