import RPi.GPIO as GPIO
import time

motorPin = (18, 23, 24, 25)
rolePerMinute = 15
stepsPerRevolution = 2048
stepSpeed = (60 / rolePerMinute) / stepsPerRevolution

pin_levels = [
    (1, 0, 0, 1),
    (1, 1, 0, 0),
    (0, 1, 1, 0),
    (0, 0, 1, 1)
]

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    for i in motorPin:
        GPIO.setup(i, GPIO.OUT)

def rotary():
    for level in pin_levels:
        for i in range(4):
            GPIO.output(motorPin[i], level[i])
            time.sleep(0.01)

def destroy():
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        while True:
            rotary()
    except KeyboardInterrupt:
        destroy()
