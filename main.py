import rtmidi.midiutil as midiutil
import time
import pigpio

class App:
    def main():
        RED_PIN = 17
        GREEN_PIN = 22
        BLUE_PIN = 24

        params = {r: 0, g: 0, b: 0, MAX: 255}

        pi = pigpio.pi()

        midiin, port_name = midiutil.open_midiinput(1)
        midiin.set_callback(this)

        this.actions = []
        this.inputs = []

        actionRedChannel = ActionRedChannel(self.params)
        self.actions.append(actionRedChannel)
        self.inputs.append(InputControl(actionRedChannel, "knob", 4))

        while True:
            
            for action in self.actions:
                action.update(params)

            for action in self.actions:
                self.params.r += action.keys["R"]
                self.params.g += action.keys["G"]
                self.params.b += action.keys["B"]

            self.params.r = min(self.params.r, self.params.MAX)
            self.params.g = min(self.params.g, self.params.MAX)
            self.params.b = min(self.params.b, self.params.MAX)

            pi.set_PWM_dutycycle(RED_PIN, self.params.r)
            pi.set_PWM_dutycycle(GREEN_PIN, self.params.g)
            pi.set_PWM_dutycycle(BLUE_PIN, self.params.b)
        print("Goodbye!")

    def __call__(self, event, data=None):
        message, deltatime = event

        print(message)
        vel = message[0]
        key = message[1]
        state = message[2]

        for midiInput in self.inputs:
            if(midiInput.key == key):
                if(midiInput.type == "trigger" and state != 0 ):
                    midiInput.trigger(self.params)
                if(midiInput.type == "toggle" and state != 0):
                    midiInput.toggle(self.params)
                if(midiInput.type == "hold"):
                    midiInput.hold(self.params, state > 0)
                if(midiInput.type == "knob"):
                    midiInput.knob(self.params, state * 2)

App().main()
