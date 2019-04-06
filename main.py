
import rtmidi.midiutil as midiutil
import time
import pigpio

def main():
    RED_PIN = 17
    GREEN_PIN = 22
    BLUE_PIN = 24

    strobe = False
    strobei = 1

    pi = pigpio.pi()
    pi.set_PWM_dutycycle(GREEN_PIN, 100)

    midiin, port_name = midiutil.open_midiinput(1)

    while True:
        midiInput = midiin.get_message()

        if midiInput:
            msg, delta = midiInput
            print(msg[1])
            if msg[1] == 48:
                strobe = True
            if msg[1] == 3:
                pi.set_PWM_dutycycle(RED_PIN, msg[2] * 2 * strobei)
            if msg[1] == 4:
                pi.set_PWM_dutycycle(GREEN_PIN, msg[2] * 2 * strobei)
            if msg[1] == 5:
                pi.set_PWM_dutycycle(BLUE_PIN, msg[2] * 2 * strobei)
            print(msg)
            

        if strobe:
            if strobei == 1:
                strobei = 0
            else:
                strobei = 1
    print("HELLO")

if __name__ == "__main__": main()
