############################################################
# Dp used
# Runs in time O(N)
############################################################

file = open("inputs/coins2.in", "r")
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
    min = 100000000000000000
    if x not in d:
        if x > coins[3]:
            if min > d[x-coins[3]]+1:
                min = d[x-coins[3]]+1
        if x > coins[2]:
            if min > d[x-coins[2]]+1:
                min = d[x-coins[2]]+1
        if x > coins[1]:
            if min > d[x-coins[1]]+1:
                min = d[x-coins[1]]+1
        if x > coins[0]:
            if min > d[x-coins[0]]+1:
                min = d[x-coins[0]]+1
        d[x] = min
print d[val]
############################################################
# finds solution of value minus each coin, checks which is
# smallest.
############################################################
