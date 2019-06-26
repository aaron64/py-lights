from actions.ActionColor import ActionColor
from actions.ActionStrobe import ActionStrobe
from actions.ActionStrobeMute import ActionStrobeMute
from actions.ActionColorTrigger import ActionColorTrigger
from actions.ActionMute import ActionMute
from actions.ActionChaos import ActionChaos
from actions.ActionKeys import ActionKeys

from Color import Color

def initialize(app, params):
    # Set GPIO pins for R, G, B wires
    params["PIN_R"] = 17
    params["PIN_G"] = 22
    params["PIN_B"] = 24

    # Create Actions
    actionWhite = app.addAction(ActionColor(params))
    actionBlue = app.addAction(ActionColor(params, Color(0, 0, 255)))
    actionStrobe = app.addAction(ActionStrobe(params))
    actionStrobeMute = app.addAction(ActionStrobeMute(params))
    actionMute = app.addAction(ActionMute(params))
    actionChaos = app.addAction(ActionChaos(params)) 
    actionKeys = app.addAction(ActionKeys(params, 48, 72, Color.red(), Color.blue()))

    # Bind Inputs to Actions
    app.addInput(actionMute, "hold", 45, "On")
    app.addInput(actionChaos, "hold", 44, "Intensity")
    app.addInput(actionWhite, "hold", 46, "Intensity")
    app.addInput(actionStrobeMute, "hold", 47, "On")

    app.addInput(actionBlue, "knob", 3, "Intensity")
    app.addInput(actionStrobe, "knob", 7, "Intensity")
    app.addInput(actionStrobe, "knob", 8, "Speed")
    app.addInput(actionStrobeMute, "knob", 10, "Speed")