# PiZeroTurret
A Raspberry Pi (Zero 2W) port of the HackPack Arduino Nano-based IT Turret project. For more:
https://www.crunchlabs.com/products/ir-turret

## Pinout
Here is the pinout diagram for the Raspberry Pi Zero 2W:

![Raspberry Pi Zero 2W Pinout](./doc/GPIO-Pinout-Diagram-2.png)

More information available at [raspberrypi.com](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html) and [pinout.xyz](https://pinout.xyz/)


Four pins are required for this project. 3 PWM outputs are required for controlling the Pitch (up/down), Yaw (swing side to side) and Roll (cannon fire mechanism) degrees of freedom. One GPIO configured as an input is required for the IR interface for decoding remote control input. To learn about pinconfig on Raspberry Pi you can look [here](https://www.raspberrypi.com/documentation/computers/config_txt.html#gpio-control).

The following table shows the connections required, the GPIO pin label for software, and the use in this code.

| Usage | 40-Pin Header | BCM GPIO Pin |
| --- | --- | --- |
| Pitch Servo | 12 | GPIO18 / PWM0 |
| Yaw Servo | 33 | GPIO13 / PWM1 | 
| Roll Servo (Firing mechanism) | 11 | GPIO17 / PWM0 |
| IR Sense input | 13 | GPIO27 |

## Python modules

The module `gpiozero`, `pulseio`, `board`, and `adafruit_irremote` are required for this project. Much (all?) are pulled in through the `adafruit_circuitpython` install procedures documented [here](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi). It was a pain in the ass. YMMV. I ended up using PIP to install the `blinka` package and it installed most of what is required under the covers. However, it was a frustrating experience. The default raspbian (headless) python/pip interaction seems to be broken as they attempt to force people to use python virtual environments. This makes sense on a development system where packages can come and go and don't always play nicely together, but makes little-to-no sense on an embedded controller where you are trying to get to a densely packed environment. But I digress. You may have to do some wayfinding to get the packages installed properly. I did, and I've been using python for 15 years.

## IRCommands Class

A class that creates a function table and a decoder method. Main benefit is that dictionary lookups are marginally faster than an extensive if/else ladder, and it's much cleaner runtime code.
To use, add a list of commands using the `addCommand` method, defining the code, in this case the IR command code index 2, a function name, and a reference to the function. To use, simply pass the code into the class with the function you want to map to that code. At runtime, call the `execCommand` method on your IR code.

Quick note on NEC encoding. The 3rd byte (index 2 if you're new) is the byte you care about. Byte 4 should be the bitwise-inverse of byte 3, but tbh I haven't checked.  


Still a WIP.  

