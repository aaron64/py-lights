import rtmidi.midiutil as midiutil
import time
import pigpio

from actions.ActionRedChannel import ActionRedChannel
from actions.ActionGreenChannel import ActionGreenChannel
from actions.ActionBlueChannel import ActionBlueChannel
from actions.ActionStrobe import ActionStrobe
from actions.ActionStrobeMute import ActionStrobeMute
from actions.ActionColorTrigger import ActionColorTrigger

from midi_in.InputControl import InputControl

class App:
    def addAction(self, action):
        self.actions.append(action)
        return action

    def addInput(self, action, type, key, setting):
        self.inputs.append(InputControl(action, type, key, setting))

    def main(self):
        RED_PIN = 17
        GREEN_PIN = 22
        BLUE_PIN = 24

        self.params = {"R": 0, "G": 0, "B": 0, "MAX": 255, "Counter": 1}

        pi = pigpio.pi()

        midiin, port_name = midiutil.open_midiinput(1)
        midiin.set_callback(self)

        self.actions = []
        self.inputs = []

        actionRedChannel = self.addAction(ActionRedChannel(self.params))
        actionGreenChannel = self.addAction(ActionGreenChannel(self.params))
        actionBlueChannel = self.addAction(ActionBlueChannel(self.params))
        actionStrobe = self.addAction(ActionStrobe(self.params))
        actionStrobeMute = self.addAction(ActionStrobeMute(self.params))
        actionColorTrigger = self.addAction(ActionColorTrigger(self.params))

        self.addInput(actionRedChannel, "knob", 3, "Val")
        self.addInput(actionGreenChannel, "knob", 4, "Val")
        self.addInput(actionBlueChannel, "hold", 48, "Val")
        self.addInput(actionStrobe, "knob", 7, "Intensity")
        self.addInput(actionStrobe, "knob", 8, "Speed")
        self.addInput(actionStrobeMute, "hold", 51, "On")
        self.addInput(actionStrobeMute, "knob", 10, "Speed")
        self.addInput(actionColorTrigger, "trigger", 60, "")

        while True:
            self.params["Counter"] += 1

            self.params["R"] = 0
            self.params["G"] = 0
            self.params["B"] = 0
            self.params["VISIBILITY"] = 1
            
            for action in self.actions:
                action.update(self.params)

            for action in self.actions:
                self.params["R"] += action.settings["R"]
                self.params["G"] += action.settings["G"]
                self.params["B"] += action.settings["B"]
                if action.settings["MUTE"] == True:
                    self.params["VISIBILITY"] = 0

            self.params["R"] = min(self.params["R"], self.params["MAX"])
            self.params["G"] = min(self.params["G"], self.params["MAX"])
            self.params["B"] = min(self.params["B"], self.params["MAX"])

            pi.set_PWM_dutycycle(RED_PIN, self.params["R"] * self.params["VISIBILITY"])
            pi.set_PWM_dutycycle(GREEN_PIN, self.params["G"] * self.params["VISIBILITY"])
            pi.set_PWM_dutycycle(BLUE_PIN, self.params["B"] * self.params["VISIBILITY"])

            time.sleep(0.01)

        print("Goodbye!")

    def __call__(self, event, data=None):
        message, deltatime = event

        print(message)
        vel = message[0]
        key = message[1]
        state = message[2] * 2

        for midiInput in self.inputs:
            if(midiInput.key == key):
                if(midiInput.type == "trigger" and state != 0 ):
                    midiInput.trigger(self.params, state)
                if(midiInput.type == "toggle" and state != 0):
                    midiInput.toggle(self.params)
                if(midiInput.type == "hold"):
                    midiInput.hold(self.params, 255 if state > 0 else 0)
                if(midiInput.type == "knob"):
                    midiInput.knob(self.params, state)

App().main()
