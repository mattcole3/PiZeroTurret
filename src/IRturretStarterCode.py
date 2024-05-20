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
pitchMin = 10
pitchMax = 175

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

def homeServos():
    servoRoll.mid()
    servoPitch.mid()
    servoYaw.mid()

def pitchUp(pitchVal=0.1):
    print("Pitching Up")
    if servoPitch.value + pitchVal <= pitchMax:
        servoPitch.value += pitchVal
    else:
        servoPitch.value = pitchMax
        print("Pitch at maximum")

def pitchDown(pitchVal=0.1):
    print("Pitching Down")
    if servoPitch.value - pitchVal >= pitchMin:
        servoPitch.value -= pitchVal
    else:
        servoPitch.value = pitchMin
        print("Pitch at minimum")

def yawLeft(yawVal=1):
    print("Yawing Left")
    servoYaw.value = servoYaw.min()
    sleep(0.06*yawVal)
    servoYaw.value = servoYaw.mid()

def yawRight(yawVal=1):
    print("Yawing Right")
    servoYaw.value = servoYaw.max()
    sleep(0.06*yawVal)
    servoYaw.value = servoYaw.mid()

def yawFiveRight():
    yawRight(5)

def yawSixLeft():
    yawLeft(5)


def setup():
    print("Setting up command list")
    cmdTable.addCommand(0x18, "UP", pitchUp())
    cmdTable.addCommand(0x10, "LEFT", yawLeft())
    cmdTable.addCommand(0x5A, "RIGHT", yawRight())
    cmdTable.addCommand(0x4A, "DOWN", pitchDown())
    cmdTable.addCommand(0x38, "OK", fire())
    cmdTable.addCommand(0xB0, "#", homeServos())
    cmdTable.addCommand(0x02, "5", yawFiveRight())
    cmdTable.addCommand(0xC2, "6", yawSixLeft())


    print("Registered ", cmdTable.count(), " Commands")
    print(cmdTable)
    
    print("Setting up IR Turret")
    homeServos()
    print("Setup Complete")

def loop():
    print("Looping")
    while True:
        pulses = decoder.read_pulses(pulsein)
        try:
            code = decoder.decode_bits(pulses)
            print("Code: ", hex(code))
            cmdTable.execCommand(code)
            
        except adafruit_irremote.IRNECRepeatException:
            print("Repeat Code")
        except adafruit_irremote.IRDecodeException as e:
            print("Failed to decode: ", e)

def main():
    setup()
    loop()

if __name__ == "__main__":
    main()