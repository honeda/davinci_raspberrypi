import RPi.GPIO as GPIO
import time

LedPin = 17
BtnPin = 18

Led_status = True

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LedPin, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(BtnPin, GPIO.IN)
    print(BtnPin)

def swLed(ev=None):
    global Led_status
    Led_status = not Led_status
    GPIO.output(LedPin, Led_status)
    if Led_status:
        print("LED OFF")
    else:
        print("LED ON")

def main():
    # GPIO.FALLINGで立ち下りエッジを検出.(HIGH->LOW)
    GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=swLed)
    while True:
        time.sleep(1)

def destroy():
    GPIO.output(LedPin, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()