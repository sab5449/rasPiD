from motor import motors
from multiprocessing import Pool
import curses

motorUnit=motors()
stdscr = curses.initscr()

motorUnit.clean()    
curses.nocbreak()
stdscr.keypad(0)
stdscr.nodelay(0)
curses.echo()
curses.endwin()
