import RPi.GPIO as gpio
import time

#Variables
trig = 36
echo = 37

#Turn on sensor and calculate distance of object
def distance(measure='cm'):
    gpio.setmode(gpio.BOARD)
    gpio.setup(trig, gpio.OUT)
    gpio.setup(echo, gpio.IN)

    #Make sure sensor isn't on or else it gets messy
    gpio.output(trig, False)

    #Turn sensor on
    gpio.output(trig, True)
    time.sleep(0.00001)
    gpio.output(trig, False)

    while gpio.input(echo) == 0:
        nosig = time.time()

    while gpio.input(echo) == 1:
        sig = time.time()

    t1 = sig - nosig

    if measure == 'cm':
        distance = t1 / 0.000058
    elif measure == 'in':
        distance = t1 / 0.000148
    else:
        print('improper measurement choice')
        distance = None

    gpio.cleanup()
    return distance
