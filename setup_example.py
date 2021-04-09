from ActionBuilder import ActionBuilder

from actions.ActionColor import ActionColor
from actions.ActionChaser import ActionChaser
from actions.ActionStrobe import ActionStrobe
from actions.ActionStrobeMask import ActionStrobeMask
from actions.ActionMask import ActionMask
from actions.ActionChaos import ActionChaos
from midi_in.Trigger import Trigger

from rpi_ws281x import Color
from colors import *

def initialize(app, params):
    # Create Actions
    actionWhite   = ActionColor(params, WHITE)
    actionRed     = ActionColor(params, RED, mask="x%2==1")
    actionGreen   = ActionColor(params, GREEN)
    actionBlue    = ActionColor(params, BLUE, mask="x%2==0")
    actionCyan    = ActionChaser(params, CYAN, mask="x%12==0")
    actionMagenta = ActionChaser(params, MAGENTA, mask="x%12==6")
    actionMagenta.settings["Velocity"] = -0.1
    actionYellow  = ActionColor(params, YELLOW)
    
    actionStrobe     = ActionStrobe(params, mask=None)
    actionStrobeMask = ActionStrobeMask(params)
    actionMask       = ActionMask(params)
    actionChaos      = ActionChaos(params)

    envelope = {
        "attack":  100,
        "decay":   150,
        "sustain": 0.9,
        "release": 150
    }

    glitterEnvelope = {
        "attack":  5,
        "decay":   15,
        "sustain": 1,
        "release": 15
    }

    strobeEnvelope = {
        "attack":  1,
        "decay":   1,
        "sustain": 1,
        "release": 1
    }


    for i in range(24):
        mask = "x%24=="+str(i)
        action = ActionColor(params, WHITE, mask=mask)
        app.addTrigger(Trigger(action, i+60, glitterEnvelope, control="Intensity"))

    # Bind Inputs to Actions
    app.addTrigger(Trigger(actionWhite, 48, envelope, control="Intensity"))
    app.addTrigger(Trigger(actionCyan, 46, envelope, control="Intensity"))
    app.addTrigger(Trigger(actionMagenta, 45, envelope, control="Intensity"))
    app.addTrigger(Trigger(actionYellow, 44, envelope, control="Intensity"))

    app.addTrigger(Trigger(actionStrobeMask, 51, None, control="Intensity"))
    app.addTrigger(Trigger(actionStrobe, 50, strobeEnvelope, control="Intensity"))
    app.addTrigger(Trigger(actionChaos, 47, None, control="Intensity"))
    app.addTrigger(Trigger(actionMask, 49, None, control="Intensity"))
