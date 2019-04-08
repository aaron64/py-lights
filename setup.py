

def initialize_actions(app, params):
    actionWhite = app.addAction(ActionColor(params))
    actionGreen = app.addAction(ActionColor(params))
    actionBlue = app.addAction(ActionColor(params, Color(0, 0, 255)))
    actionStrobe = app.addAction(ActionStrobe(params))
    actionStrobeMute = app.addAction(ActionStrobeMute(params))
    actionMute = app.addAction(ActionMute(params))
    actionChaos = app.addAction(ActionChaos(params))

    app.addInput(actionWhite, "hold", 46, "Intensity")
    app.addInput(actionGreen, "knob", 3, "Intensity")
    app.addInput(actionBlue, "knob", 4, "Intensity")
    app.addInput(actionStrobe, "knob", 7, "Intensity")
    app.addInput(actionStrobe, "knob", 8, "Speed")
    app.addInput(actionStrobeMute, "hold", 47, "On")
    app.addInput(actionStrobeMute, "knob", 10, "Speed")
    app.addInput(actionMute, "hold", 45, "On")
    app.addInput(actionChaos, "hold", 44, "Intensity")

    ActionBuilder.buildKeys(app, 48, 72, Color.red(), Color.blue())
