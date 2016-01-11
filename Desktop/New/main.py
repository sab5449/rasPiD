import Fusion as position
from motor import motors
from threading import Thread
import math




motorUnit = motors()
#maxDuty is the period
Duty=0.005
motorUnit.maxDuty=0.005
motorUnit.increment=0.00015
motorUnit.setDuty(Duty)


if __name__ == '__main__':
    t1=Thread(target=motorUnit.motorOneP)
    t2=Thread(target=motorUnit.motorTwoP)
    t3=Thread(target=motorUnit.motorThreeP)
    t4=Thread(target=motorUnit.motorFourP)
    t1.setDaemon(True)
    t2.setDaemon(True)
    t3.setDaemon(True)
    t4.setDaemon(True)
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    while True:
        fusionPose = position.getPos();
        

        #pitch test
        if fusionPose != None:
            print math.degrees(fusionPose[1])
            if math.degrees(fusionPose[1]) > 2:
                #decrease front motor speed
                motorUnit.keyInDecoder(115)
                motorUnit.keyInDecoder(102)
                #increase back motor speed
                motorUnit.keyInDecoder(101)
                motorUnit.keyInDecoder(116) 
            elif math.degrees(fusionPose[1]) < -2:
                #decrease back motor speed
                motorUnit.keyInDecoder(100)
                motorUnit.keyInDecoder(103)
                #increase front motor speed
                motorUnit.keyInDecoder(119)
                motorUnit.keyInDecoder(114)

                        
        
