class Motors:
    def __init__():
        print "Setting motor parameters!"
        #motor one
        Motor1A = 37
        Motor1B = 38
        Motor1E = 40
        #motor two
        Motor2A = 33
        Motor2B = 35
        Motor2E = 36
        #motor 3
        Motor3A = 29
        Motor3B = 31
        Motor3E = 32
        #motor 4
        Motor4A = 15
        Motor4B = 16
        Motor4E = 18
        #set up outpins
        GPIO.setup(Motor1A, GPIO.OUT)
        GPIO.setup(Motor1B, GPIO.OUT)
        GPIO.setup(Motor1E, GPIO.OUT)

        GPIO.setup(Motor2A, GPIO.OUT)
        GPIO.setup(Motor2B, GPIO.OUT)
        GPIO.setup(Motor2E, GPIO.OUT)

        GPIO.setup(Motor3A, GPIO.OUT)
        GPIO.setup(Motor3B, GPIO.OUT)
        GPIO.setup(Motor3E, GPIO.OUT)

        GPIO.setup(Motor4A, GPIO.OUT)
        GPIO.setup(Motor4B, GPIO.OUT)
        GPIO.setup(Motor4E, GPIO.OUT)

        

    #BEGIN METHODS#
    

    def motorOneOn():
        print "Motor 1 on"
        GPIO.output(Motor1A, GPIO.HIGH)
        GPIO.output(Motor1B, GPIO.LOW)
        GPIO.output(Motor1E, GPIO.HIGH)
    def motorTwoOn():
        print "Motor 2 on"
        GPIO.output(Motor2A, GPIO.HIGH)
        GPIO.output(Motor2B, GPIO.LOW)
        GPIO.output(Motor2E, GPIO.HIGH)
    def motorThreeOn():
        print "Motor 3 on"
        GPIO.output(Motor3A, GPIO.HIGH)
        GPIO.output(Motor3B, GPIO.LOW)
        GPIO.output(Motor3E, GPIO.HIGH)
    def motorFourOn():
        print "Motor 4 on"
        GPIO.output(Motor4A, GPIO.HIGH)
        GPIO.output(Motor4B, GPIO.LOW)
        GPIO.output(Motor4E, GPIO.HIGH)

    def motorOneOff():
        print "Motor 1 off"
        GPIO.output(Motor1E, GPIO.LOW)
    def motorTwoOff():
        print "Motor 2 off"
        GPIO.output(Motor2E, GPIO.LOW)
    def motorThreeOff():
        print "Motor 3 off"
        GPIO.output(Motor3E, GPIO.LOW)
    def motorFourOff():
        print "Motor 4 off"
        GPIO.output(Motor4E, GPIO.LOW)

