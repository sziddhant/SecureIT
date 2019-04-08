import time
from server import *
import digitalio
import board
import adafruit_matrixkeypad
import RPi.GPIO as GPIO
import time
cols = [digitalio.DigitalInOut(x) for x in (board.D26, board.D20, board.D21)]
rows = [digitalio.DigitalInOut(x) for x in (board.D5, board.D6, board.D13, board.D19)]


keys = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        ('*', 0, '#'))

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50)  # GPIO 17 for PWM with 50Hz
p.start(2.5)  # Initialization

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

def open_door():
    # run servo
    servoPIN = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 50)  # GPIO 17 for PWM with 50Hz
    p.start(2.5)
    try:
        p.ChangeDutyCycle(7.5)
        time.sleep(1)
        p.ChangeDutyCycle(0)
    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()
    print('Welcome!')
    return

def key_in():
    y=0
    vc=4
    while True and vc:
        keys = keypad.pressed_keys
        if keys:
            print("Pressed: ", keys)
            vc = vc - 1
            zz = int(keys[0])
            y = y + (zz * pow(10,vc))
        time.sleep(0.2)
    print(y)
    return y

def pass_verify(x):
        print(x)
        otp_inp = key_in()
        if otp_inp== x:
            print(x)
            open_door()
            return 1
        else:
            #short buzz

            pass_verify(x)

            return 1



