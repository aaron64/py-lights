from ActionBuilder import ActionBuilder

from actions.ActionColor import ActionColor
from actions.ActionStrobe import ActionStrobe
from actions.ActionStrobeMask import ActionStrobeMask
from actions.ActionColorTrigger import ActionColorTrigger
from actions.ActionMask import ActionMask
from actions.ActionChaos import ActionChaos



def initialize(app, params):
    # Set GPIO pins for R, G, B wires
    params["PIN_R"] = 17
    params["PIN_G"] = 22
    params["PIN_B"] = 24

    # Create Actions
    actionWhite = app.addAction(ActionColor(params))
    actionBlue = app.addAction(ActionColor(params, Color(0, 0, 255)))
    actionStrobe = app.addAction(ActionStrobe(params))
    actionStrobeMask = app.addAction(ActionStrobeMask(params))
    actionMute = app.addAction(ActionMask(params))
    actionChaos = app.addAction(ActionChaos(params))

    # Bind Inputs to Actions
    app.addTrigger(actionMute, "hold", 45, "On")
    app.addTrigger(actionChaos, "hold", 44, "Intensity")
    app.addTrigger(actionWhite, "hold", 46, "Intensity")
    app.addTrigger(actionStrobeMask, "hold", 47, "On")

    app.addTrigger(actionBlue, "knob", 3, "Intensity")
    app.addTrigger(actionStrobe, "knob", 7, "Intensity")
    app.addTrigger(actionStrobe, "knob", 8, "Speed")
    app.addTrigger(actionStrobeMask, "knob", 10, "Speed")


    # Use ActionBuilder (optional)
    ActionBuilder.buildKeys(app, 48, 72, Color.red(), Color.blue())
