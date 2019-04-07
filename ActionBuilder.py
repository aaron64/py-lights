from actions.ActionColorTrigger import ActionColorTrigger
from Color import Color

class ActionBuilder():

	@staticmethod
	buildKeys(params, actions, inputs, low, high, color=Color.white()):
		for i in range(low, high):
			action = ActionColorTrigger(params, color)
			actions.append(action)
			inputs.append(InputControl(action, type, i, ""))