import time
import pid

#KP = 1.0
#KI = 1.0
#KD = 1.0

print("Desired Height")
endHeight = float(input())



location = []
location = list()
#list of error values

trapezoids = 0

while(True):
    currentHeight = pid.getHeight()
    error = endHeight - currentHeight

    proportional = error * pid.KP


    if len(location) == 0 or location[-1] <= 0.01:
        #once ideal height obtained, stop expanding list
        location.append(error)
    if len(location)>1:
        derivative = (location[-1]*pid.KD-location[-2]*pid.KD)/0.5
    #calculates derivative based off of height 0.5 seconds ago
    #Each error is multiplied by KD

    
    if len(location)<2:
        pid.setThrust(proportional)
        #starting height is zero, integral = 0
    elif len(location)<3:
        trapezoids = 0.25*(2*(location[-1]*pid.KI*2))
        pid.setThrust(derivative+trapezoids+proportional)
        trapezoids = location[-1]*pid.KI
        #handles case when there is one collumn
    else:
        trapezoids += (location[-1]*pid.KI + location[-2]*pid.KI)
        pid.setThrust(0.25*(trapezoids)+derivative+proportional)
    #uses trapezoid rule to calculate integral
    print error
    time.sleep(0.5)
