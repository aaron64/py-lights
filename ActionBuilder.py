from actions.ActionColorTriggerHold import ActionColorTriggerHold
from Color import Color
from midi_in.InputControl import InputControl

class ActionBuilder():

	@staticmethod
	def buildKeys(app, low, high, col1=Color.white(), col2=Color.white(), attack=0, release=0):
        high += 1
		for i in range(low, high):
			color = Color.interpolate(col1, col2, (float(i-low)/(high-low)))
			action = ActionColorTriggerHold(app.params, color)
			app.actions.append(action)
			app.inputs.append(InputControl(action, "trigger_hold", i, ""), attack=attack, release=release)