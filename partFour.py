# DP used
# runs in time O(N) where N is number of nodes(r*c)
file = open("sum.in", "r")
input = file.readline()
input = input.rstrip()
input = input.split(" ")
yval = int(input[0])
xval = int(input[1])

info = []
new = set()
nodes = []
for x in range(int(input[0])):
    temp = []
    for y in range(int(input[1])):
        temp.append(-1)
    nodes.append(temp)
    line = file.readline()
    line = line.rstrip()
    line = line.split(" ")
    info.append(line)
file.close()

# info are the dist. for each path
# nodes are the current values, with -1 being unvisited
# parent keeps track of the parent node of the position that is being occupied

def updateSurroundings(tempy,tempx):
    if tempx < xval-1:  
        #right
        if nodes[tempy][tempx] + int(info[tempy][tempx+1]) < nodes[tempy][tempx+1] or nodes[tempy][tempx+1] == -1:
            nodes[tempy][tempx+1] = nodes[tempy][tempx] + int(info[tempy][tempx+1])
            new.add((tempy,tempx+1))
    if tempx > 0:
        #left
        if nodes[tempy][tempx] + int(info[tempy][tempx-1]) < nodes[tempy][tempx-1] or nodes[tempy][tempx-1] == -1:
            nodes[tempy][tempx-1] = nodes[tempy][tempx] + int(info[tempy][tempx-1])
            new.add((tempy,tempx-1))
    if tempy > 0:
        #above
        if nodes[tempy][tempx] + int(info[tempy-1][tempx]) < nodes[tempy-1][tempx] or nodes[tempy-1][tempx] == -1:
            nodes[tempy-1][tempx] = nodes[tempy][tempx] + int(info[tempy-1][tempx])
            new.add((tempy-1,tempx))
    if tempy < yval-1:
        #below
        if nodes[tempy][tempx] + int(info[tempy+1][tempx]) < nodes[tempy+1][tempx] or nodes[tempy+1][tempx] == -1:
            nodes[tempy+1][tempx] = nodes[tempy][tempx] + int(info[tempy+1][tempx])
            new.add((tempy+1,tempx))
#updates list to surrounding nodes

#main
nodes[0][0] = int(info[0][0]) 
currentx = 0
currenty = 0
updateSurroundings(0,0)

while nodes[yval-1][xval-1] == -1:    
    current = set(new)
    new.clear()
    for x in range(len(current)):
        coord = current.pop()
        updateSurroundings(coord[0],coord[1])
    print nodes[0]
    print nodes[1]
    print nodes[2]
    print nodes[3]
    print nodes[4]
    print " "
#    if nodes[yval][xval] != -1:
#        i += 1


print nodes[0]
print nodes[1]
print nodes[2]
print nodes[3]
print nodes[4]
