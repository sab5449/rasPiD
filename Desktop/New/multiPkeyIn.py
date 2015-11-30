from motor import motors
from multiprocessing import Pool
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
Duty=0.005
motorUnit.maxDuty=0.005
motorUnit.increment=0.00015
motorUnit.setDuty(Duty)






if __name__ == '__main__':
    pool = Pool(processes=4)
    #press w to decel
    #press s to accel
    
while (userInput != 27):
        #get the keyboard press ascii code
    userInput = stdscr.getch()

    if userInput != -1:
        motorUnit.keyInDecoder(userInput)

        
    
    pool.apply_async(motorUnit.motorOneP())
    pool.apply_async(motorUnit.motorTwoP())
    #pool.apply_async(motorUnit.motorThreeP())
    #pool.apply_async(motorUnit.motorFourP())
 
        
        
motorUnit.clean()    
curses.nocbreak()
stdscr.keypad(0)
stdscr.nodelay(0)
curses.echo()
curses.endwin()
