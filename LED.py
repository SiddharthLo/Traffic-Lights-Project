import RPi.GPIO as GPIO
import time

sensor = 21
buzzer = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)

count = 0

try:
    while True:
        if GPIO.input(sensor):
            count = count + 1
            while GPIO.input(sensor):
                time.sleep(0.2)
            print(count)

except KeyboardInterrupt:
    GPIO.cleanup()
