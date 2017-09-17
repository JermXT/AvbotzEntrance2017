import time

KP = 1.0
KI = 1.0
KD = 1.0

print("Desired Height")
endHeight = float(input())

def getHeight():
    #returns a float
    return
def setThrust(thrust):
    return

location = []
location = list()
#list of error values

trapezoids = 0
while(True):
    currentHeight = getHeight()
    error = endHeight - currentHeight

    proportional = error * KP

    if location[-1] <= 0.01:
        #once ideal height obtained, stop expanding list
        location.append(error)
    

    derivative = (location[-1]*KD-location[-2]*KD)/0.5
    #calculates derivative based off of height 0.5 seconds ago
    #Each error is multiplied by KD

    
    if len(location)<2:
        setThrust(derivative+proportional)
        #starting height is zero, integral = 0
    elif len(location)<3:
        trapezoids = 0.25(2*(location[-1]*KI*2))
        setThrust(derivative+integral+proportional)
        trapezoids = location[-1]*KI
        #handles case when there is one collumn
    else:
        trapezoids += (location[-1]*KI + location[-2]*KI)
        setThrust(0.25(trapezoids)+derivative+proportional)
    #uses trapezoid rule to calculate integral
    
    time.sleep(0.5)
