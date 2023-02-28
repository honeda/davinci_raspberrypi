import RPi.GPIO as GPIO
import time

tilt_pin = 17
led_pin_1 = 27
led_pin_2 = 22


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(tilt_pin, GPIO.IN)
    GPIO.setup(led_pin_1, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(led_pin_2, GPIO.OUT, initial=GPIO.HIGH)

def main():
    while True:
        if GPIO.input(tilt_pin) == 1:
            print("LED_1 ON")
            GPIO.output(led_pin_1, GPIO.LOW)
            GPIO.output(led_pin_2, GPIO.HIGH)
        if GPIO.input(tilt_pin) == 0:
            print("LED_2 ON")
            GPIO.output(led_pin_2, GPIO.LOW)
            GPIO.output(led_pin_1, GPIO.HIGH)

        time.sleep(.5)

def destroy():
    GPIO.output(led_pin_1, GPIO.HIGH)
    GPIO.output(led_pin_2, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()
