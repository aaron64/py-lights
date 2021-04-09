from ActionBuilder import ActionBuilder

from actions.ActionColor import ActionColor
from actions.ActionChaser import ActionChaser
from actions.ActionStrobe import ActionStrobe
from actions.ActionStrobeMask import ActionStrobeMask
from actions.ActionMask import ActionMask
from actions.ActionChaos import ActionChaos
from actions.ActionRainbow import ActionRainbow
from midi_in.Trigger import Trigger, TriggerTypes

from rpi_ws281x import Color
from colors import *

def initialize(app, params):
	# Create Actions
	actionWhite   = ActionColor(params, WHITE)
	actionRed     = ActionColor(params, RED)
	actionGreen   = ActionColor(params, GREEN)
	actionBlue    = ActionColor(params, BLUE)
	actionCyan    = ActionChaser(params, CYAN, mask="x%12==6")
	actionMagenta = ActionChaser(params, MAGENTA, mask="x%12==0")
	actionMagenta.settings["Velocity"] = -0.1
	actionYellow  = ActionColor(params, YELLOW)
	
	actionStrobe     = ActionStrobe(params, mask=None)
	actionStrobeMask = ActionStrobeMask(params)
	actionMask       = ActionMask(params)
	actionChaos      = ActionChaos(params)
	actionRainbow    = ActionRainbow(params)

	envelope = {
		"attack":  100,
		"decay":   150,
		"sustain": 0.9,
		"release": 300
	}

	glitterEnvelope = {
		"attack":  100,
		"decay":   15,
		"sustain": 1,
		"release": 250
	}

	strobeEnvelope = {
		"attack":  1,
		"decay":   1,
		"sustain": 1,
		"release": 1
	}


	for i in range(24):
		mask = "x%12=="+str(i)
		action = ActionColor(params, WHITE, mask=mask)
		app.addTrigger(Trigger(action, i+60, glitterEnvelope, control="Intensity"))

	# Bind Inputs to Actions
	app.addTrigger(Trigger(actionRed, 53, envelope, control="Intensity"))
	app.addTrigger(Trigger(actionGreen, 54, envelope, control="Intensity"))
	app.addTrigger(Trigger(actionBlue, 55, envelope, control="Intensity"))
	app.addTrigger(Trigger(actionCyan, 56, envelope, control="Intensity"))
	app.addTrigger(Trigger(actionMagenta, 57, envelope, control="Intensity"))
	app.addTrigger(Trigger(actionYellow, 58, envelope, control="Intensity"))

	app.addTrigger(Trigger(actionWhite, 48, envelope, control="Intensity"))

	app.addTrigger(Trigger(actionCyan, 46, envelope, control="Intensity"))
	app.addTrigger(Trigger(actionMagenta, 45, envelope, control="Intensity"))

	app.addTrigger(Trigger(actionStrobe, 3, control="Speed", type=TriggerTypes.Knob, knob_lambda="(1,1000)"))
	app.addTrigger(Trigger(actionStrobe, 4, control="Intensity", type=TriggerTypes.Knob))
	app.addTrigger(Trigger(actionStrobeMask, 5, control="Speed", type=TriggerTypes.Knob, knob_lambda="(1,1000)"))
	app.addTrigger(Trigger(actionStrobeMask, 6, control="Intensity", type=TriggerTypes.Knob))

	app.addTrigger(Trigger(actionRainbow, 7, control="Speed", type=TriggerTypes.Knob, knob_lambda="(0,1)"))
	app.addTrigger(Trigger(actionRainbow, 8, control="Intensity", type=TriggerTypes.Knob))

	app.addTrigger(Trigger(actionCyan, 10, control="Velocity", type=TriggerTypes.Knob, knob_lambda="(-5, 5)"))
	app.addTrigger(Trigger(actionMagenta, 10, control="Velocity", type=TriggerTypes.Knob, knob_lambda="(5, -5)"))

	app.addTrigger(Trigger(actionMask, 9, control="Intensity", type=TriggerTypes.Knob))

	app.addTrigger(Trigger(actionStrobeMask, 51, None, control="Intensity"))
	app.addTrigger(Trigger(actionStrobe, 50, strobeEnvelope, control="Intensity"))
	app.addTrigger(Trigger(actionChaos, 44, None, control="Intensity"))
	app.addTrigger(Trigger(actionRainbow, 47, None, control="Intensity"))
	app.addTrigger(Trigger(actionMask, 49, None, control="Intensity"))

	# app.addTrigger(Trigger(actionBlue, 3, envelope, control="Intensity"))
	# app.addTrigger(Trigger(actionStrobe, 8, envelope, control="SPEED"))


	# Use ActionBuilder (optional)
	# ActionBuilder.buildKeys(app, 48, 72, RED, BLUE)
