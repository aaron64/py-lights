import rtmidi.midiutil as midiutil
import time
import pigpio

from setup import initialize

from midi_in.InputControl import InputControl
from midi_in.InputLogger import InputLogger
from LEDStrip import clear_LEDs
from Color import Color

class App:
    def addAction(self, action):
        self.actions.append(action)
        return action

    def addInput(self, action, type, key, setting):
        midiInput = InputControl(action, type, key, setting)
        self.inputs.append(midiInput)
        self.inputLogger.addInput(midiInput)

    def main(self):
        print("Starting py-lights...")

        LED_COUNT      = 16
        LED_PIN       = 18
        LED_FREQ_HZ    = 800000
        LED_DMA        = 10
        LED_BRIGHTNESS = 255
        LED_INVERT     = False
        LED_CHANNEL    = 0

        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        strip.begin()

        self.params = {
            "Counter": 1,
            "MAX": 255
        }

        self.inputLogger = InputLogger()

        self.actions = []
        self.inputs  = []
        
        self.LEDs    = []

        for i in range(LED_COUNT):
            self.LEDs.append({'R':0, 'G':0, 'B':0, 'A':1})

        initialize(self, self.params)

        # initialize midi
        print("Initializing MIDI")
        midiin, port_name = midiutil.open_midiinput(1)
        midiin.set_callback(self)

        print("Ready...")
        # Main loop
        while True:
            self.params["Counter"] += 1

            clear_LEDs(self.LEDs)
            self.params["VISIBILITY"] = 1
            
            for action in self.actions:
                action.update(self.params, LEDs)

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

        for midiInput in self.inputs:
            if(midiInput.key == key):
                if(midiInput.type == "trigger" and state != 0 ):
                    midiInput.trigger(self.params, state)
                if(midiInput.type == "trigger_hold"):
                    midiInput.triggerHold(self.params, state)
                if(midiInput.type == "toggle" and state != 0):
                    midiInput.toggle(self.params)
                if(midiInput.type == "hold"):
                    midiInput.hold(self.params, 255 if state > 0 else 0)
                if(midiInput.type == "knob"):
                    midiInput.knob(self.params, state)

App().main()
