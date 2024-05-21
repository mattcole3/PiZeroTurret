from gpiozero import Servo
from time import sleep
import pulseio
import board
import adafruit_irremote
from IRCommands import IRCommands

pulsein = pulseio.PulseIn(board.D27, maxlen=120, idle_state=True)
decoder = adafruit_irremote.GenericDecode()

servoRoll = Servo(17)
servoPitch = Servo(18)
servoYaw = Servo(13)
pitchMin = 10
pitchMax = 160

'''
Does conversion into servo scale, but include sw defined clipping. Not included in the reverse conversion.
'''
def deg_to_servo(deg, mind=0, maxd=180):
    servoRange = 180
    valRange=2
    deg = max(min(maxd, deg), mind)
    return deg/servoRange * valRange - 1

def servo_to_deg(val):
    servoRange = 180
    valRange=2
    return (val + 1) * servoRange/valRange

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
    tempVal = servo_to_deg(servoPitch.value)    
    print("TempVal: ", tempVal)
    serVal = deg_to_servo(tempVal - pitchDeg, pitchMin, pitchMax)
    print("ServoVal: ", serVal)
    servoPitch.value = serVal

def pitchDown(pitchDeg=10):
    print("Pitching Down")
    tempVal = servo_to_deg(servoPitch.value)
    print("TempVal: ", tempVal)
    serVal = deg_to_servo(tempVal + pitchDeg, pitchMin, pitchMax)
    print("ServoVal: ", serVal)
    servoPitch.value = serVal

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