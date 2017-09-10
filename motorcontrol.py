import RPi.GPIO as gpio
import time

#Initialize pins
def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(11, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    gpio.setup(16, gpio.OUT)
    gpio.setup(18, gpio.OUT)

#Helper function to send signal to motors
def setPins(p1, p2, p3, p4):
    init()
    gpio.output(11, p1)
    gpio.output(15, p2)
    gpio.output(16, p3)
    gpio.output(18, p4)


#forward = black
def forward(time_frame):
    init()
    setPins(False, True, True, False)
    time.sleep(time_frame)
    gpio.cleanup()

#back = blue
def reverse(time_frame):
    init()
    setPins(True, False, False, True)
    time.sleep(time_frame)
    gpio.cleanup()

#right turn
def right_turn(time_frame):
    init()
    setPins(False, True, False, True)
    time.sleep(time_frame)
    gpio.cleanup()

#left turn
def left_turn(time_frame):
    init()
    setPins(True, False, True, False)
    time.sleep(time_frame)
    gpio.cleanup()






                                                                                                              [ Read 52 lines ]
^G Get Help                            ^O WriteOut                            ^R Read File                           ^Y Prev Page                           ^K Cut Text                            ^C Cur Pos
^X Exit                                ^J Justify                             ^W Where Is                            ^V Next Page                           ^U UnCut Text                          ^T To Spell
