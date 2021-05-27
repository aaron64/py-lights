from core.actions.ActionColor import ActionColor
from core.actions.ActionChaser import ActionChaser
from core.actions.ActionStrobe import ActionStrobe
from core.actions.ActionStrobeMask import ActionStrobeMask
from core.actions.ActionMask import ActionMask
from core.actions.ActionChaos import ActionChaos

from core.midi_in.Trigger import Trigger

from rpi_ws281x import Color
from core.colors import *


def initialize(app, params):
    # Create Actions
    actionWhite = ActionColor(params, WHITE)
    actionRed = ActionColor(params, RED, mask="x%2==1")
    actionGreen = ActionColor(params, GREEN)
    actionBlue = ActionColor(params, BLUE, mask="x%2==0")
    actionCyan = ActionChaser(params, CYAN, mask="x%12==0")
    actionMagenta = ActionChaser(params, MAGENTA, mask="x%12==6")
    actionMagenta.settings["Velocity"] = -0.1
    actionYellow = ActionColor(params, YELLOW)

    actionStrobe = ActionStrobe(params, mask=None)
    actionStrobeMask = ActionStrobeMask(params)
    actionMask = ActionMask(params)
    actionChaos = ActionChaos(params)

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
        app.add_trigger(
            Trigger(action, i+60, glitterEnvelope, control="Intensity"))

    # Bind Inputs to Actions
    app.add_trigger(Trigger(actionWhite, 48, envelope, control="Intensity"))
    app.add_trigger(Trigger(actionCyan, 46, envelope, control="Intensity"))
    app.add_trigger(Trigger(actionMagenta, 45, envelope, control="Intensity"))
    app.add_trigger(Trigger(actionYellow, 44, envelope, control="Intensity"))

    app.add_trigger(Trigger(actionStrobeMask, 51, None, control="Intensity"))
    app.add_trigger(
        Trigger(actionStrobe, 50, strobeEnvelope, control="Intensity"))
    app.add_trigger(Trigger(actionChaos, 47, None, control="Intensity"))
    app.add_trigger(Trigger(actionMask, 49, None, control="Intensity"))
