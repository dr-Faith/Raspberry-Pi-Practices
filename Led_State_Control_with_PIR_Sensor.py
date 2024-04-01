import RPi.GPIO as GPIO
import time

PIR_PIN = 4
LED_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_PIN, GPIO.OUT)

while True:
    time.sleep(0.1)
    print(GPIO.input(PIR_PIN))
    
    if GPIO.input(PIR_PIN) == 1:
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        GPIO.output(LED_PIN, GPIO.LOW)


GPIO.cleanup()
