from gpiozero import Servo
from gpiozero import AngularServo
from time import sleep
import pulseio
import board
import adafruit_irremote
from IRCommands import IRCommands

pulsein = pulseio.PulseIn(board.D27, maxlen=120, idle_state=True)
decoder = adafruit_irremote.GenericDecode()

pitchMin = -45
pitchMax = 45

servoRoll = Servo(17)
servoPitch = AngularServo(18, min_angle=pitchMin, max_angle=pitchMax, initial_angle=5)
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

def homeServos():
    servoRoll.mid()
    servoPitch.mid()
    servoYaw.mid()

def pitchUp(pitchDeg=10):
    print("Pitching Up")
    servoPitch.value += pitchDeg

def pitchDown(pitchDeg=10):
    print("Pitching Down")
    servoPitch.value -= pitchDeg

def yawLeft(yawVal=5):
    print("Yawing Left")
    servoYaw.value = 1
    sleep(0.06*yawVal)
    servoYaw.mid()

def yawRight(yawVal=5):
    print("Yawing Right")
    servoYaw.value = -1
    sleep(0.06*yawVal)
    servoYaw.mid()

def yawFiveRight():
    yawRight(75)

def yawSixLeft():
    yawLeft(75)

def setup():
    print("Setting up command list")
    cmdTable.addCommand(0x18, "UP", pitchUp)
    cmdTable.addCommand(0x10, "LEFT", yawLeft)
    cmdTable.addCommand(0x5A, "RIGHT", yawRight)
    cmdTable.addCommand(0x4A, "DOWN", pitchDown)
    cmdTable.addCommand(0x38, "OK", fire)
    cmdTable.addCommand(0xB0, "#", homeServos)
    cmdTable.addCommand(0x02, "5", yawFiveRight)
    cmdTable.addCommand(0xC2, "6", yawSixLeft)


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
            code = decoder.decode_bits(pulses)[2]
            print("Code: ", code)
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