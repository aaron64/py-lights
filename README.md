


# Py-Lights V2
Py-Lights (name pending) is a program to bind MIDI inputs different effects (actions) that output to WS2812x LEDs.

## Setup
1. Configure hardware (you can follow [this](https://tutorials-raspberrypi.com/connect-control-raspberry-pi-ws2812-rgb-led-strips/)) tutorial)
2. Get [python-rtmidi](https://pypi.org/project/python-rtmidi/) ```pip install python-rtmidi```
2. Get [rpi_ws281x](https://pypi.org/project/rpi-ws281x/) ```pip install rpi_ws281x```

## Creating your action setup
To add actions to the program, use ```setup.py``` to add actions, then add inputs to them (see ```setup_example.py```).

Inputs have 5 different modes:

|trigger |trigger_hold |toggle  |hold  |knob  |
|--|--|--|--|--|
|Activated in a single instance  |Activated in an instance and while held   |(todo)  |Activated while held  |Activated when a knob is updated  |


A list of actions can be found here. Parameters are declared on object creation as optional parameters while settings are used for variables that can change throughout use.

|Action          |Parameters (default)                                |Settings (default)                   |
|----------------|----------------------------------------------------|-------------------------------------|
|Action (base)   |                                                    |Color (black)  MUTE (False)          |
|Color           |Color (white)                                       |Intensity (0)                        |
|ColorTrigger    |Color (white)  Attack (0)  Sustain (20)  Release (0)|Attack (0)  Sustain (20)  Release (0)|
|ColorTriggerHold|Color (white)  Attack (0)   Release (0)             |Attack (0)  Release (0)              |
|Strobe          |Color (white)                                       |Intensity (0)  Speed (5)             |
|StrobeMute      |                                                    |Speed (5)  On (0)                    |
|StrobeTap       |Color (white)                                       |Intensity (0)                        |
|Mute            |                                                    |On (0)                               |
|Chaos           |                                                    |Intensity (0)                        |

## Running
To run, simply use the command ```sh init.sh```

## Contributing
Please let me know if you would like to contribute any Actions or other features! Also please inquire me about any issues or confusion in documentation.
