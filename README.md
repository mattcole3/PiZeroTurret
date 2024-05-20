# PiZeroTurret
A Raspberry Pi (Zero 2W) port of the HackPack Arduino Nano-based IT Turret project.

## Pinout
Here is the pinout diagram for the Raspberry Pi Zero 2W:

![Raspberry Pi Zero 2W Pinout](./doc/GPIO-Pinout-Diagram-2.png))

More information available 
[here](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html)

Four pins are required for this project. 3 PWM outputs are required for controlling the Pitch, Yaw and Roll(cannon fire mechanism) degrees of freedom. One GPIO configured as an input is required for the IR interface for decoding remote control input.

The following table shows the connections required, the GPIO pin label for software, and the use in this code.

| Usage | 40-Pin Header | BCM GPIO Pin |
| --- | --- | --- |
| Pitch Servo | 12 | GPIO18 / PWM0 |
| Yaw Servo | 33 | GPIO13 / PWM1 | 
| Roll Servo (Firing mechanism) | 11 | GPIO17 / PWM0 |
| IR Sense input | 13 | GPIO27 |
