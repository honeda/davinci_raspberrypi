import RPi.GPIO as GPIO
import time

BeepPin = 17

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BeepPin, GPIO.OUT, initial=GPIO.HIGH)

def beep():
    GPIO.output(BeepPin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(BeepPin, GPIO.HIGH)

def main():
    while True:
        beep()
        time.sleep(0.3)
        beep()
        time.sleep(0.3)
        beep()
        time.sleep(0.3)
        beep()
        time.sleep(0.3)

        beep()
        time.sleep(0.12)
        beep()
        time.sleep(0.12)
        beep()
        time.sleep(0.12)
        beep()
        time.sleep(0.12)
        beep()
        time.sleep(0.5)

def destroy():
    # turn off buzzer
    GPIO.output(BeepPin, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()