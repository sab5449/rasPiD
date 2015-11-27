import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

class motors:
    def __init__(self):
        print "Setting motor parameters!"
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
    

    def motorOneOn(self):
        print "Motor 1 on"
        GPIO.output(self.Motor1A, GPIO.HIGH)
        GPIO.output(self.Motor1B, GPIO.LOW)
        GPIO.output(self.Motor1E, GPIO.HIGH)
    def motorTwoOn(self):
        print "Motor 2 on"
        GPIO.output(self.Motor2A, GPIO.HIGH)
        GPIO.output(self.Motor2B, GPIO.LOW)
        GPIO.output(self.Motor2E, GPIO.HIGH)
    def motorThreeOn(self):
        print "Motor 3 on"
        GPIO.output(self.Motor3A, GPIO.HIGH)
        GPIO.output(self.Motor3B, GPIO.LOW)
        GPIO.output(self.Motor3E, GPIO.HIGH)
    def motorFourOn(self):
        print "Motor 4 on"
        GPIO.output(self.Motor4A, GPIO.HIGH)
        GPIO.output(self.Motor4B, GPIO.LOW)
        GPIO.output(self.Motor4E, GPIO.HIGH)

    def motorOneOff(self):
        print "Motor 1 off"
        GPIO.output(self.Motor1E, GPIO.LOW)
    def motorTwoOff(self):
        print "Motor 2 off"
        GPIO.output(self.Motor2E, GPIO.LOW)
    def motorThreeOff(self):
        print "Motor 3 off"
        GPIO.output(self.Motor3E, GPIO.LOW)
    def motorFourOff(self):
        print "Motor 4 off"
        GPIO.output(self.Motor4E, GPIO.LOW)

