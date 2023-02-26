import RPi.GPIO as GPIO
import time

MotorPin1 = 17
MotorPin2 = 27
MotorEnable = 22

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(MotorPin1, GPIO.OUT)
    GPIO.setup(MotorPin2, GPIO.OUT)
    GPIO.setup(MotorEnable, GPIO.OUT, initial=GPIO.LOW)

def motor(direction):
    # Clockwise
    if direction == 1:
        GPIO.output(MotorPin1, GPIO.HIGH)
        GPIO.output(MotorPin2, GPIO.LOW)

        GPIO.output(MotorEnable, GPIO.HIGH)
        print("Clockwise")
    # Counterclockwise
    if direction == -1:
        GPIO.output(MotorPin1, GPIO.LOW)
        GPIO.output(MotorPin2, GPIO.HIGH)

        GPIO.output(MotorEnable, GPIO.HIGH)
        print("Counterclockwise")
    # Stop
    if direction == 0:
        GPIO.output(MotorEnable, GPIO.LOW)
        print("Stop")

def main():
    directions = {"CW": 1, "CCW": -1, "STOP": 0}
    while True:
        motor(directions["CW"])
        time.sleep(5)

        motor(directions["STOP"])
        time.sleep(2)

        motor(directions["CCW"])
        time.sleep(5)

        motor(directions["STOP"])
        time.sleep(2)

def destroy():
    GPIO.output(MotorEnable, GPIO.LOW)
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()
