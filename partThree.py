############################################################
# Dp used
# Runs in time O(N^2)
############################################################

file = open("coins2.in", "r")
input = file.readline()
file.close()
input = input.rstrip()
input = input.split(' ')
coins = []

val = int(input[0])
temp = val

for x in range(1,5):
    coins.append(int(input[x]))
coins.sort()

############################################################
# Dictionary to store values:solutions 
############################################################
d = {1:1}
d[coins[1]] = 1
d[coins[2]] = 1
d[coins[3]] = 1

############################################################
# Finds solution of current value by iterating through
# solutions of previous values
############################################################


for x in range(2, val+1):
    if x not in d:
        if x % 2 != 0:
            len= (x-1)/2
        else:
            len = x/2
        y = 1
        while y < len+1:
            temp = d[y]+d[x-y]
            if(y == 1 or temp < min):
                
                min = temp
            y += 1
        d[x] = min
        
file = open("coins2.out", "w")

file.write("%s" % (d[val]))
file.close()


        
    

