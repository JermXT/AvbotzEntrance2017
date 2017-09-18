############################################################
# Pid takes the error values and calculates the thrust of
# the quadcopter. Error*constant grows proportionally as
# error becomes small, and helps accelerate in order to 
# achieve the correct height. The derivative of the error
# helps slow down the quadcopter as it approches the correct
# height; the slope becomes negative when the error is 
# decreasing. Last, the integral stops the quadcopter from
# oscillating back and forth; once it has achieved the right
# thrust, proportional and derivative are both zero, and the
# integral is the area under the curve of the error, which 
# will remain  constant because error is zero.
############################################################   
import time
import pid

print("Desired Height")
endHeight = float(input())

location = []
location = list()
#list of error values

trapezoids = 0

#----------------------------------------------------------- 
# Calculates Proportional, Integral, and Derivative every
# 0.5 seconds. Adds these together to detirmine the thrust
# of the quadcopter.
#----------------------------------------------------------- 
while(True):
    currentHeight = pid.getHeight()
    error = endHeight - currentHeight

    proportional = error * pid.KP


    if len(location) == 0 or location[-1] <= 0.01:
        # once ideal height has been obtained, stop expanding list
        location.append(error)

    if len(location)>1:
        derivative = (location[-1]*pid.KD-location[-2]*pid.KD)/0.5
        # calculates derivative based off of height 0.5 seconds ago
        # Each error is multiplied by KD

    
    if len(location)<2:
        pid.setThrust(proportional)
        # starting height is zero, integral = 0, no derivative
    elif len(location)<3:
        trapezoids = (location[-1]*pid.KI)*0.5*0.5
        pid.setThrust(derivative+trapezoids+proportional)
        # handles case when there is one collumn
    else:
        trapezoids += 0.25*(location[-1]*pid.KI + location[-2]*pid.KI)
        pid.setThrust(trapezoids+derivative+proportional)
        # uses trapezoid rule to calculate integral
    print error
    time.sleep(0.5)
