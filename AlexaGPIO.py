from flask import Flask
from flask_ask import Ask, statement, convert_errors
from time import sleep
import RPi.GPIO as GPIO
import logging

GPIO.setmode(GPIO.BCM)

app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

locationDict = {
    'blue': 25,
    'green': 24,
    'red': 23,
    'white': 22
}

@ask.launch
def gpio_start():
    initGPIO()
    for key in locationDict:
        GPIO.output(locationDict[key], GPIO.HIGH)
        sleep(0.2)
        GPIO.output(locationDict[key], GPIO.LOW)

    return statement('Wellcome to GPIO test application')

@ask.intent('LocationControlIntent', mapping={'status': 'status', 'location': 'location'})
def location_control(status, location):
    initGPIO()
    if location in locationDict:
        targetPin = locationDict[location]

        if status in ['on', 'high']:        GPIO.output(targetPin, GPIO.HIGH)
        if status in ['off', 'low']:        GPIO.output(targetPin, GPIO.LOW)
    elif location == "all":
        turnAll(status)
    else:
        return statement('Unkown command!')

    return statement('Turning {} {}!'.format(location, status))

@ask.intent('PlayIntent')
def play_intent():
    initGPIO()
    play()
    return statement('Hey! Looks at the leds')


def turnAll(status):
    for key in locationDict:
        if status in ['on', 'high']:
            GPIO.output(locationDict[key], GPIO.HIGH)
        if status in ['off', 'low']:
            GPIO.output(locationDict[key], GPIO.LOW)

def play():
    gpios = list(locationDict.values())
    for key in gpios:
        GPIO.output(key, GPIO.HIGH)
        sleep(0.2)
    for key in gpios[::-1]:
        GPIO.output(key, GPIO.LOW)
        sleep(0.2)
    for key in gpios:
        GPIO.output(key, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(key, GPIO.LOW)
        sleep(0.2)
    for key in gpios:
        GPIO.output(key, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(key, GPIO.LOW)
        sleep(0.1)
        GPIO.output(key, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(key, GPIO.LOW)

def initGPIO():
    for key in locationDict:
        GPIO.setup(locationDict[key], GPIO.OUT)

if __name__ == '__main__':
    app.run(debug=True)
