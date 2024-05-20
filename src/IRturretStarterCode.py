from gpiozero import Servo
from time import sleep
import pulseio
import board
import adafruit_irremote
from IRcommands import IRCommands

pulsein = pulseio.PulseIn(board.D27, maxlen=120, idle_state=True)
decoder = adafruit_irremote.GenericDecode()

servoRoll = Servo(17)
servoPitch = Servo(18)
servoYaw = Servo(13)

cmdTable = IRCommands()

'''
# This is the code for the IR turret
'''

'''
# Local variables mapping labels to codes
codes = {
    '1': 0xA2,
    '2': 0x62,
    '3': 0xE2,
    '4': 0x22,
    '5': 0x02,
    '6': 0xC2,
    '7': 0xE0,
    '8': 0xA8,
    '9': 0x90,
    '0': 0x98,
    '*': 0x68,
    '#': 0xB0,
    'UP': 0x18,
    'LEFT': 0x10,
    'RIGHT': 0x5A,
    'DOWN': 0x4A,
    'OK': 0x38
}
'''

def fire():
    print("Firing")
    servoRoll.min()
    sleep(0.5)
    servoRoll.mid()

void homeServos():
    servoRoll.mid()
    servoPitch.mid()
    servoYaw.mid()


def setup():
    print("Setting up command list")
    cmdTable.addCommand(0x18, "UP", pitchUp())
    cmdTable.addCommand(0x10, "LEFT", yawLeft())
    cmdTable.addCommand(0x5A, "RIGHT", yawRight())
    cmdTable.addCommand(0x4A, "DOWN", pitchDown())
    cmdTable.addCommand(0x38, "OK", fire())
    cmdTable.addCommand(0xB0, "#", homeServos())
    
    print("Setting up IR Turret")
    servoRoll.mid()
    servoPitch.mid()
    servoYaw.mid()
    print("Setup Complete")

def loop():
    print("Looping")
    while True:
        pulses = decoder.read_pulses(pulsein)
        try:
            code = decoder.decode_bits(pulses)
            print("Code: ", hex(code))




            '''
            if code == codes['UP']:
                print("UP")
                servoPitch.min()
            elif code == codes['LEFT']:
                print("LEFT")
                servoYaw.min()
            elif code == codes['RIGHT']:
                print("RIGHT")
                servoYaw.max()
            elif code == codes['DOWN']:
                print("DOWN")
                servoPitch.max()
            elif code == codes['OK']:
                print("OK")
                fire()
                sleep(0.2)
            else:
                print("Invalid Code")
                print("UP")
                servoPitch.min()
            '''
        except adafruit_irremote.IRNECRepeatException:
            print("Repeat Code")
        except adafruit_irremote.IRDecodeException as e:
            print("Failed to decode: ", e)

def main():
    setup()
    loop()

if __name__ == "__main__":
    main()