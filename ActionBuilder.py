from actions.ActionColorTrigger import ActionColorTrigger
from Color import Color

from midi_in.InputControl import InputControl

class ActionBuilder():

	@staticmethod
	def buildKeys(params, actions, inputs, low, high, col1=Color.white(), col2=Color.white()):
                high += 1
		for i in range(low, high):
			color = Color.interpolate(col1, col2, (float(i-low)/(high-low)))
			action = ActionColorTrigger(params, color)
			actions.append(action)
			inputs.append(InputControl(action, "trigger", i, ""))
