from motor import motors
from time import sleep
import curses


stdscr = curses.initscr()
stdscr.nodelay(1)
curses.noecho()
curses.cbreak()
stdscr.keypad(1)

userInput = None
currentInput=None

motorUnit = motors()
#maxDuty is the period
maxDuty=0.05
duty=maxDuty
duty2=maxDuty
duty3=maxDuty
duty4=maxDuty
motorUnit.maxDuty=duty
increment=0.0015
#press w to decel
#press s to accel
while (userInput != 27):
    #get the keyboard press ascii code
    userInput = stdscr.getch()

    #only detect a keyboard hit one time
    #otherwise do nothing
    if (userInput!= currentInput):
        currentInput=userInput
    else:
        currentInput=-1
        
    #determine the course of action based on keyboard input
    if (currentInput==119):
        duty += increment
        #duty cannot be greater than period
        if (duty > maxDuty):
            duty = maxDuty
    elif(currentInput==115):
        duty -= increment
        #time cannot be negative
        if (duty < 0):
            duty = 0
            
    #control for motor number two        
    if (currentInput==101):
        duty2 += increment
        if (duty2 > maxDuty):
            duty2 = maxDuty
    elif(currentInput==100):
        duty2 -= increment
        if (duty2 < 0):
            duty2 = 0

    #control for motor number three       
    if (currentInput==114):
        duty3 += increment
        if (duty3 > maxDuty):
            duty3 = maxDuty
    elif(currentInput==102):
        duty3 -= increment
        if (duty3 < 0):
            duty3 = 0

    #control for motor number four       
    if (currentInput==116):
        duty4 += increment
        if (duty4 > maxDuty):
            duty4 = maxDuty
    elif(currentInput==103):
        duty4 -= increment
        if (duty4 < 0):
            duty4 = 0
            
    #call the motor pulse methods        
    motorUnit.motorOneP(duty)
    motorUnit.motorTwoP(duty2)
    motorUnit.motorThreeP(duty3)
    motorUnit.motorFourP(duty4)
    
        
        
motorUnit.clean()    
curses.nocbreak()
stdscr.keypad(0)
stdscr.nodelay(0)
curses.echo()
curses.endwin()
