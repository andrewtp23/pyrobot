import motorcontrol
import soundsensor
import random

while True:
    #Always move forward
    motorcontrol.forward(0.2)
    #If close to object, backup
    dist = soundsensor.distance('cm')
    print(dist)
    if soundsensor.distance('cm') <= 20:
        motorcontrol.reverse(0.5)
        #Randomly turn then loop again
        turn = random.randint(0,9) % 2
        if random.randint == 0:
            motorcontrol.left_turn(random.randint(0,9) % 2)
        else:
            motorcontrol.right_turn(random.randint(0,9) % 2)
