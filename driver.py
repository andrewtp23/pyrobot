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










































^G Get Help                            ^O WriteOut                            ^R Read File                           ^Y Prev Page                           ^K Cut Text                            ^C Cur Pos
^X Exit                                ^J Justify                             ^W Where Is                            ^V Next Page                           ^U UnCut Text                          ^T To Spell
