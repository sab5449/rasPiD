import motor
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)


motorControl = Motors()

while keyIn != "Esc":
    if msvcrt.kbhit():
        print "Key pressed: %s" %msvcrt.getch()
        

GPIO.cleanup()
