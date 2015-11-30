import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

class motors:
    def __init__(self):
        print "Setting motor parameters!"
        #run continuous factor
        self.maxDuty=None
        self.increment=None
        self.duty=None
        self.duty2=None
        self.duty3=None
        self.duty4=None
        #motor one
        self.Motor1A = 37
        self.Motor1B = 38
        self.Motor1E = 40
        #motor two
        self.Motor2A = 33
        self.Motor2B = 35
        self.Motor2E = 36
        #motor 3
        self.Motor3A = 29
        self.Motor3B = 31
        self.Motor3E = 32
        #motor 4
        self.Motor4A = 11
        self.Motor4B = 13
        self.Motor4E = 15
        #set up outpins
        GPIO.setup(self.Motor1A, GPIO.OUT)
        GPIO.setup(self.Motor1B, GPIO.OUT)
        GPIO.setup(self.Motor1E, GPIO.OUT)

        GPIO.setup(self.Motor2A, GPIO.OUT)
        GPIO.setup(self.Motor2B, GPIO.OUT)
        GPIO.setup(self.Motor2E, GPIO.OUT)

        GPIO.setup(self.Motor3A, GPIO.OUT)
        GPIO.setup(self.Motor3B, GPIO.OUT)
        GPIO.setup(self.Motor3E, GPIO.OUT)

        GPIO.setup(self.Motor4A, GPIO.OUT)
        GPIO.setup(self.Motor4B, GPIO.OUT)
        GPIO.setup(self.Motor4E, GPIO.OUT)

        

    #BEGIN METHODS#

    #cleanup method
    def clean(self):
        GPIO.cleanup()
    def setDuty(self,maxD):
        self.duty=maxD
        self.duty2=maxD
        self.duty3=maxD
        self.duty4=maxD

    def motorOneOn(self):
        print ("Motor 1 on")
        GPIO.output(self.Motor1A, GPIO.HIGH)
        GPIO.output(self.Motor1B, GPIO.LOW)
        GPIO.output(self.Motor1E, GPIO.HIGH)
    def motorTwoOn(self):
        print ("Motor 2 on")
        GPIO.output(self.Motor2A, GPIO.HIGH)
        GPIO.output(self.Motor2B, GPIO.LOW)
        GPIO.output(self.Motor2E, GPIO.HIGH)
    def motorThreeOn(self):
        print ("Motor 3 on")
        GPIO.output(self.Motor3A, GPIO.HIGH)
        GPIO.output(self.Motor3B, GPIO.LOW)
        GPIO.output(self.Motor3E, GPIO.HIGH)
    def motorFourOn(self):
        print ("Motor 4 on")
        GPIO.output(self.Motor4A, GPIO.HIGH)
        GPIO.output(self.Motor4B, GPIO.LOW)
        GPIO.output(self.Motor4E, GPIO.HIGH)

    def motorOneOff(self):
        print ("Motor 1 off")
        GPIO.output(self.Motor1E, GPIO.LOW)
    def motorTwoOff(self):
        print ("Motor 2 off")
        GPIO.output(self.Motor2E, GPIO.LOW)
    def motorThreeOff(self):
        print ("Motor 3 off")
        GPIO.output(self.Motor3E, GPIO.LOW)
    def motorFourOff(self):
        print ("Motor 4 off")
        GPIO.output(self.Motor4E, GPIO.LOW)
    #Begin pulse methods
    def motorOneP(self):
        print ("\nMotor 1 pulsing at freq: " + str(self.duty) + "\n")
        GPIO.output(self.Motor1A, GPIO.HIGH)
        GPIO.output(self.Motor1B, GPIO.LOW)
        GPIO.output(self.Motor1E, GPIO.HIGH)
        #time spent on
        sleep(self.maxDuty-self.duty)
        GPIO.output(self.Motor1E, GPIO.LOW)
        #time spent off
        sleep(self.duty)

    def motorTwoP(self):
        print ("\nMotor 2 pulsing at freq: " + str(self.duty2) + "\n")
        GPIO.output(self.Motor2A, GPIO.HIGH)
        GPIO.output(self.Motor2B, GPIO.LOW)
        GPIO.output(self.Motor2E, GPIO.HIGH)
        #time spent on
        sleep(self.maxDuty-self.duty2)
        GPIO.output(self.Motor2E, GPIO.LOW)
        #time spent off
        sleep(self.duty2)
        
    def motorThreeP(self):
        print ("\nMotor 3 pulsing at freq: " + str(self.duty3) + "\n")
        GPIO.output(self.Motor3A, GPIO.HIGH)
        GPIO.output(self.Motor3B, GPIO.LOW)
        GPIO.output(self.Motor3E, GPIO.HIGH)
        #time spent on
        sleep(self.maxDuty-self.duty3)
        GPIO.output(self.Motor3E, GPIO.LOW)
        #time spent off
        sleep(self.duty3)

    def motorFourP(self):
        print ("\nMotor 3 pulsing at freq: " + str(self.duty4) + "\n")
        GPIO.output(self.Motor4A, GPIO.HIGH)
        GPIO.output(self.Motor4B, GPIO.LOW)
        GPIO.output(self.Motor4E, GPIO.HIGH)
        #time spent on
        sleep(self.maxDuty-self.duty4)
        GPIO.output(self.Motor4E, GPIO.LOW)
        #time spent off
        sleep(self.duty4)

#input decoder experiemental
    def keyInDecoder(self, keyPress):
        if (keyPress==119):
            self.duty += self.increment
            #duty cannot be greater than period
            if (self.duty > self.maxDuty):
                self.duty = self.maxDuty
        elif(keyPress==115):
            self.duty -= self.increment
            #time cannot be negative
            if (self.duty < 0):
                self.duty = 0       
        #control for motor number two        
        elif (keyPress==101):
            self.duty2 += self.increment
            if (self.duty2 > self.maxDuty):
                self.duty2 = self.maxDuty
        elif(keyPress==100):
            self.duty2 -= self.increment
            if (self.duty2 < 0):
                self.duty2 = 0
        #control for motor number three       
        elif (keyPress==114):
            self.duty3 += self.increment
            if (self.duty3 > self.maxDuty):
                self.duty3 = self.maxDuty
        elif(keyPress==102):
            self.duty3 -= self.increment
            if (self.duty3 < 0):
                self.duty3 = 0
        #control for motor number four       
        elif (keyPress==116):
            self.duty4 += self.increment
            if (self.duty4 > self.maxDuty):
                self.duty4 = self.maxDuty
        elif(keyPress==103):
            self.duty4 -= self.increment
            if (self.duty4 < 0):
                self.duty4 = 0
            

