import RPi.GPIO as gpio
from urllib import request
import json
from time import sleep


try:
    gpio.setmode(gpio.BCM)

    gpio.setup(18, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)

    while True:
        with request.urlopen("http://www.ide50-ckarthik114.cs50.io/data") as url:
            data = json.loads(url.read().decode())
            led1 = data[0]['led1']
            led2 = data[0]['led2']
            led3 = data[0]['led3']

            if led1 == "on":
                gpio.output(18, gpio.HIGH)

            else:
                gpio.output(18, gpio.LOW)

            if led2 == "on":
                gpio.output(23, gpio.HIGH)

            else:
                gpio.output(23, gpio.LOW)

            if led3 == "on":
                gpio.output(24, gpio.HIGH)

            else:
                gpio.output(24, gpio.LOW)

            print(data)

            sleep(2.5)

except:
    gpio.cleanup()

