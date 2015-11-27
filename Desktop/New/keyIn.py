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

maxDuty=0.05
duty=maxDuty
motorUnit.maxDuty=duty
increment=0.0015

while (userInput != 27):
    #get the keyboard press ascii code
    userInput = stdscr.getch()

    #only detect a keyboard hit one time
    #otherwise do nothing
    if (userInput!= currentInput):
        currentInput=userInput
    else:
        currentInput=-1
        
    if (currentInput==119):
        duty += increment
        if (duty > maxDuty):
            duty = maxDuty
    elif(currentInput==115):
        duty -= increment
        #time cannot be negative
        if (duty < 0):
            duty = 0
    
    motorUnit.motorOneP(duty)
    
        
        
motorUnit.clean()    
curses.nocbreak()
stdscr.keypad(0)
stdscr.nodelay(0)
curses.echo()
curses.endwin()
