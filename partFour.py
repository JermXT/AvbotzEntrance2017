# DP used
# runs in time O(N) where N is number of nodes(r*c)
file = open("sum.in", "r")
input = file.readline()
input = input.rstrip()
input = input.split(" ")
y = int(input[0])
x = int(input[1])

info = []

nodes = []
parent = []
for x in range(int(input[0])):
    temp = []
    hemp = []
    for y in range(int(input[1])):
        temp.append(-1)
        hemp.append(-1)
    nodes.append(temp)
    parent.append(hemp)
    line = file.readline()
    line = line.rstrip()
    line = line.split(" ")
    info.append(line)
file.close()

# info are the dist. for each path
# nodes are the current values, with -1 being unvisited
# parent keeps track of the parent node of the position that is being occupied


coordx = 0
coordy = 0
nodes[0][0] = int(info[0][0])
curr = int(info[0][0])
print nodes
print "    "

while [coordx, coordy] != [r-1, c-1]:
    print [coordx, coordy]
    if coordy < c-1:
        right = nodes[coordx][coordy+1]
        rval = int(info[coordx][coordy+1])
    else:
        right = -2
        rval = 0
        
    if coordx < r-1:
        below = nodes[coordx+1][coordy]
        bval = int(info[coordx+1][coordy])
    else:
        below = -2
        bval = 0
    
    #print int(info[coordx][coordy+1])+curr
    #print int(info[coordx+1][coordy])+curr
    if(right > rval+curr or right == -1):
        a = int(info[coordx][coordy+1])+curr
        
        nodes[coordx][coordy+1] = a
        
        parent[coordx][coordy+1] = [coordx, coordy]
    if(below > bval+curr or below == -1):
        a = int(info[coordx+1][coordy])+curr
        nodes[coordx+1][coordy] = a
        
        parent[coordx+1][coordy] = [coordx, coordy]
    #print("right, below", nodes[coordx][coordy+1], nodes[coordx+1][coordy])
    
    if rval > bval and coordy < c-1:
        
        coordy +=1
        #curr += nodes[coordx+1][coordy]
    elif bval >= rval and coordx < r-1:
        coordx+=1
        #curr += nodes[coordx][coordy+1]
    elif coordy == c-1:
        coordx += 1
    elif coordx == r-1:
        coordy += 1
    print nodes

    
    
print nodes
print coordx, coordy
