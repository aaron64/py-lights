from actions.ActionColorTrigger import ActionColorTrigger
from midi_in.InputControl import InputControl
from Color import Color

class ActionBuilder:

	@staticmethod
	def buildKeys(params, actions, inputs, low, high, color=Color.white()):
		for i in range(low, high):
                        print i
			action = ActionColorTrigger(params, color)
			actions.append(action)
			inputs.append(InputControl(action, "trigger", i, ""))
