from BirdBrain import Finch
import turtle as Faiz
import time

f = Finch('A')
Faiz.width(3)
Faiz.color("red")
Faiz.speed(10)

veered_off = False

def lineFollowingScenarios_TEST (requiredReading, turnDegree):
    while veered_off == False:
        readingRight = f.getLine('R')
        readingLeft = f.getLine('L')
        if readingRight > requiredReading:
            f.setTurn('L', turnDegree, 10)
        elif readingLeft > requiredReading:
            f.setTurn('R', turnDegree, 10)

def stopwatch_timeElapsed ():
    pass

#################################################################################################################################################

while veered_off == False:
    f.setMotors(5,5)
    x = f.getLine('R')
    y = f.getLine('L')
    distance_to_wall = f.getDistance()

    f.setBeak(100,30,86)
    if f.getButton('A'):
        break

    check95_right = False    
    check60_right = False
    check35_right = False
    check10_right = False
    check95_left = False
    check60_left = False
    check35_left = False
    check10_left = False

    if x < 95:
        f.setTurn('R',3,20)
        Faiz.right(4)
        check95_right = True    
        check60_right = False
        check35_right = False
        check10_right = False
        check95_left = False
        check60_left = False
        check35_left = False
        check10_left = False
    elif y < 95:
        f.setTurn('L',3,20)
        Faiz.left(4)
        check95_right = False    
        check60_right = False
        check35_right = False
        check10_right = False
        check95_left = True
        check60_left = False
        check35_left = False
        check10_left = False
    
    if x < 60:
        f.setTurn('R',15,20)
        Faiz.right(18)
        check95_right = False    
        check60_right = True
        check35_right = False
        check10_right = False
        check95_left = False
        check60_left = False
        check35_left = False
        check10_left = False
    elif y < 60:
        f.setTurn('L',15,20)
        Faiz.left(18)  
        check95_right = False    
        check60_right = False
        check35_right = False
        check10_right = False
        check95_left = False
        check60_left = True
        check35_left = False
        check10_left = False
    
    if x < 35:
        f.setTurn('R',30,20)
        Faiz.right(30)
        check95_right = False    
        check60_right = False
        check35_right = True
        check10_right = False
        check95_left = False
        check60_left = False
        check35_left = False
        check10_left = False
    elif y < 35:
        f.setTurn('L',30,20)
        Faiz.left(30)       
        check95_right = False    
        check60_right = False
        check35_right = False
        check10_right = False
        check95_left = False
        check60_left = False
        check35_left = True
        check10_left = False
    
    if x < 10:
        f.setTurn('R',50,20)
        Faiz.right(50)
        check95_right = False    
        check60_right = False
        check35_right = False
        check10_right = True
        check95_left = False
        check60_left = False
        check35_left = False
        check10_left = False
    elif y < 10:
        f.setTurn('L',50,20)
        Faiz.left(50)
        check95_right = False    
        check60_right = False
        check35_right = False
        check10_right = False
        check95_left = False
        check60_left = False
        check35_left = False
        check10_left = True
    
    elif distance_to_wall <= 7.5:
        veered_off = True
    
    elif check95_right == False and  check60_right == False and check35_right == False and check10_right == False and check95_left == False and check60_left == False and check35_left == False and check10_left == False:
        Faiz.forward (5)

#################################################################################################################################################

def getEncoder_TEST (leftWheelRotations, rightWheelRotations):
    f.setMotors(leftWheelRotations,rightWheelRotations)
    f.resetEncoders()
    time.sleep(1)
    print("Right wheel: " + str(f.getEncoder('R')))
    print("Left wheel: " + str(f.getEncoder('L')))

#getEncoder_TEST(0,50)\\\
f.stopAll()


