import rtmidi.midiutil as midiutil
import time
import pigpio
import uuid

from setup import initialize
from webUI import initialize_ui

from midi_in.InputControl import InputControl
from midi_in.InputLogger import InputLogger
from Color import Color

class App:
    def addAction(self, action):
        self.actions[uuid.uuid4().hex] = action
        return action

    def addInput(self, action, _type, key, setting):
        midiInput = InputControl(uuid.uuid4().hex, action, _type, key, setting)
        action.addInput(midiInput)
        self.inputs[midiInput.id] = midiInput
        self.inputLogger.addInput(midiInput)

    def main(self):
        print("Starting py-lights...")

        self.params = {
            "R": 0,
            "G": 0, 
            "B": 0, 
            "MIN": 0,
            "MAX": 255, 
            "Counter": 1,
            "PIN_R": 0,
            "PIN_G": 0,
            "PIN_B": 0
        }

        self.inputLogger = InputLogger()

        self.actions = {}
        self.inputs = {}

        # initialize actions, bindings
        initialize(self, self.params)

        # initialize gpio
        print("Initializing GPIO")
        pi = pigpio.pi()

        # initialize midi
        print("Initializing MIDI")
        midiin, port_name = midiutil.open_midiinput(1)
        midiin.set_callback(self)

        # initialize web UI
        initialize_ui(self)

        print("Ready...")
        # Main loop
        while True:
            self.params["Counter"] += 1

            self.params["R"] = 0
            self.params["G"] = 0
            self.params["B"] = 0
            self.params["VISIBILITY"] = 1
            
            for _id, action in self.actions.items():
                action.update(self.params)

            for _id, action in self.actions.items():
                self.params["R"] += action.outputColor.r
                self.params["G"] += action.outputColor.g
                self.params["B"] += action.outputColor.b
                if action.mute:
                    self.params["VISIBILITY"] = 0

            self.params["R"] = min(self.params["R"], self.params["MAX"])
            self.params["G"] = min(self.params["G"], self.params["MAX"])
            self.params["B"] = min(self.params["B"], self.params["MAX"])

            pi.set_PWM_dutycycle(self.params["PIN_R"], self.params["R"] * self.params["VISIBILITY"])
            pi.set_PWM_dutycycle(self.params["PIN_G"], self.params["G"] * self.params["VISIBILITY"])
            pi.set_PWM_dutycycle(self.params["PIN_B"], self.params["B"] * self.params["VISIBILITY"])

            time.sleep(0.01)

        print("Goodbye!")

    def __call__(self, event, data=None):
        message, deltatime = event

        print(message)
        vel = message[0]
        key = message[1]
        state = message[2] * 2

        for _id, midiInput in self.inputs.items():
            if(midiInput.key == key):
                if(midiInput.type == "trigger" and state != 0 ):
                    midiInput.trigger(self.params, state)
                if(midiInput.type == "trigger_hold"):
                    midiInput.triggerHold(self.params, state)
                if(midiInput.type == "toggle" and state != 0):
                    midiInput.toggle(self.params, state)
                if(midiInput.type == "hold", state):
                    midiInput.hold(self.params, 255 if state > 0 else 0)
                if(midiInput.type == "knob"):
                    midiInput.knob(self.params, state)

App().main()
