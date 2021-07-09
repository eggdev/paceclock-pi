import RPi.GPIO as GPIO
import time

RED_PIN = 7
GREEN_PIN = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(RED_PIN, GPIO.OUT)

for x in range(500):
    GPIO.output(RED_PIN, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(RED_PIN, GPIO.LOW)
    time.sleep(2)

GPIO.cleanup()
