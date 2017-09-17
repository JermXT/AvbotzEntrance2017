file = open("coins.in", "r")
input = file.readline()
file.close()
val = float(input)
val = val*100
val = int(val)
coins = 0

while(val > 0):
    if(val  >= 25):
        val -= 25
        coins += 1
        
    if(val >= 10 and val < 25):
        val -= 10
        coins += 1
        
    if(val >= 5 and val < 10):
        a -= 5
        coins += 1
        
    if(val >= 1 and val < 5):
        val -= 1
        coins += 1
        
file = open("coins.out", "w")
file.write("%s" % (coins))
file.close()

