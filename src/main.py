#!/usr/bin/python3

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

import rtmidi.midiutil as midiutil
import time

from setup import initialize

from core.midi_in.Trigger import *

from core.utils.strip_utils import clear_LEDs, correct_gamma
from rpi_ws281x import *

import threading

from core.context import context

# context.led_count = 109
# context.led_count = 60
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0

# app = Flask(__name__)
# bootstrap = Bootstrap(app)


# @app.route('/')
# def index():
#     print(APPLICATION.get_payload())
#     return render_template('index.html', data=APPLICATION.get_payload())


class App:
    def __init__(self):
        self.triggers = []
        self.actions = []
        self.entities = []

    def register_trigger(self, trigger):
        self.triggers[trigger.key].append(trigger)

    def register_action(self, action):
        if action not in self.actions:
            self.actions.append(action)

    def add_entity(self, entity):
        self.entities.append(entity)

    def main(self):
        print("Starting py-lights...")

        for i in range(context.key_count):
            self.triggers.append([])

        initialize(self)

        strip = Adafruit_NeoPixel(
            context.led_count, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        strip.begin()

        clear_LEDs(strip, context.led_count)
        strip.show()

        # initialize midi
        print("Initializing MIDI")
        midiutil.list_input_ports()
        midiin, port_name = midiutil.open_midiinput(1)
        # midiin2, port_name = midiutil.open_midiinput(2)
        midiin.set_callback(self)
        # midiin2.set_callback(self)

        print("Ready...")
        # Main loop
        while True:
            start = time.time()

            clear_LEDs(strip, context.led_count)

            # Update
            for triggers in self.triggers:
                for trigger in triggers:
                    if trigger.state != TriggerStates.Idle:
                        trigger.update()

            entity_remove_list = []
            for entity in self.entities:
                entity.update()
                if entity.finished:
                    entity_remove_list.append(entity)

            for entity in entity_remove_list:
                self.entities.remove(entity)

            for action in self.actions:
                if action.is_on():
                    action.update()

            # Render
            for action in self.actions:
                if action.is_on():
                    action.render(strip)

            for entity in self.entities:
                entity.render(strip)

            for action in self.actions:
                if action.is_on():
                    action.render_post(strip)

            correct_gamma(strip)

            strip.show()

            time_dif = time.time() - start
            if time_dif < 0.016:
                time.sleep(0.016 - time_dif)
            # print(time.time() - start)

        print("Goodbye!")

    def get_payload(self):
        return {
            "actions": list(map(Action.to_dict, self.actions)),
            "triggers": [list(map(Trigger.to_dict, x)) for x in self.triggers]
        }

    def __call__(self, event, data=None):
        message, deltatime = event

        state = message[0]
        key = message[1]
        velocity = message[2]/128

        if state == 128:
            velocity = 0

        # print(state, key, velocity)

        for map_key, triggers in enumerate(self.triggers):
            for trigger in triggers:
                if(map_key == key):
                    if trigger.type == TriggerTypes.Key or trigger.type == TriggerTypes.Toggle:
                        if velocity > 0:
                            trigger.trigger(self, velocity)
                        else:
                            trigger.key_up()
                    elif trigger.type == TriggerTypes.Knob:
                        trigger.knob(velocity)


if __name__ == '__main__':
    context.application = App()
    thread = threading.Thread(target=context.application.main)
    thread.start()
    # app.run(debug=True, host='0.0.0.0', port=8085, use_reloader=False)
