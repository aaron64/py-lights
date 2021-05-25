


# Py-Lights V2
Py-Lights is a program to bind MIDI inputs different effects (actions) that output to WS2812x LEDs.

## Setup
1. Configure hardware (you can follow [this](https://tutorials-raspberrypi.com/connect-control-raspberry-pi-ws2812-rgb-led-strips/)) tutorial)
2. Get [python-rtmidi](https://pypi.org/project/python-rtmidi/) ```pip install python-rtmidi```
2. Get [rpi_ws281x](https://pypi.org/project/rpi-ws281x/) ```pip install rpi_ws281x```

## Creating your action setup
To add actions to the program, use ```setup.py``` to add actions, then add inputs to them (see ```setup_example.py```).

Triggers have 3 different types:

|Key (default)                                     |Toggle                               |Knob                              |
|--------------------------------------------------|-------------------------------------|----------------------------------|
|Activated on button press, deactivated on release |Activated and decativated each tap   |Activated when a knob is updated  |


A list of actions can be found here. Parameters are declared on object creation as optional parameters while settings are used for variables that can change throughout use.

|Action          |Parameters (default)                                |Settings (default)                   |
|----------------|----------------------------------------------------|-------------------------------------|
|Bolt            |                                                    |Velocity, Position                   |
|Chaos           |                                                    |Speed                                |
|ChaosMask       |                                                    |Speed                                |
|Chaser          |                                                    |Velocity                             |
|Color           |                                                    |                                     |
|Fill            |                                                    |Speed, Position                      |
|FillMask        |                                                    |Speed, Position                      |
|Glitter         |                                                    |Speed                                |
|Mask            |                                                    |                                     |
|Mirror          |                                                    |                                     |
|Noise           |                                                    |Velocity, Width                      |
|Point           |                                                    |Position, Width                      |
|Rainbow         |                                                    |Velocity                             |
|Rings           |                                                    |Speed, Position, Spacing             |
|Strobe          |                                                    |Speed                                |
|StrobeMask      |                                                    |Speed                                |
|Wave            |                                                    |Velocity, Width                      |

## Running
To run, simply execute ```python3 main.py``` (may have to run as sudo)

## Contributing
Please let me know if you would like to contribute any Actions or other features! Also please inquire me about any issues or confusion in documentation.
