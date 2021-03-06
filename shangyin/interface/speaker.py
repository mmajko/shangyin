import RPi.GPIO as GPIO
import time

SPKR_PIN = 12

def init():
    GPIO.setup(SPKR_PIN, GPIO.OUT)

def beep(duration, tone):
    pwm = GPIO.PWM(SPKR_PIN, tone)
    pwm.start(40)
    time.sleep(duration)
    pwm.stop()

def play_intro():
    beep(0.05, 261)
    beep(0.05, 329)
    beep(0.05, 392)
    beep(0.1, 523)

def play_wait():
    beep(0.05, 261)

def play_success():
    beep(0.1, 523)