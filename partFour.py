import copy
# DP used
# runs in time O(N) where N is number of nodes(r*c)
file = open("sum.in", "r")
input = file.readline()
input = input.rstrip()
input = input.split(" ")
yval = int(input[0])
xval = int(input[1])

info = []
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
parent = copy.deepcopy(nodes)
visited = {}
file.close()

# info are the dist. for each path
# nodes are the current values, with -1 being unvisited
# parent keeps track of the parent node of the position that is being occupied

def updateSurroundings(tempy,tempx):
    closest = -1
    if tempx < xval-1:  
        #check right node
        if nodes[tempy][tempx] + int(info[tempy][tempx+1]) < nodes[tempy][tempx+1] or nodes[tempy][tempx+1] == -1:
            nodes[tempy][tempx+1] = int(info[tempy][tempx+1]) + nodes[tempy][tempx]
            parent[tempy][tempx+1] = [tempy,tempx]
            visited[tempy,tempx+1] = nodes[tempy][tempx+1]
            if int(info[tempy][tempx+1]) + nodes[tempy][tempx] < closest or closest == -1:
                closest = int(info[tempy][tempx+1]) + nodes[tempy][tempx]
                
    if tempy < yval-1:
        #check node below
        if nodes[tempy][tempx] + int(info[tempy+1][tempx]) < nodes[tempy+1][tempx] or nodes[tempy+1][tempx] == -1:
            nodes[tempy+1][tempx] = nodes[tempy][tempx] + int(info[tempy+1][tempx])
            parent[tempy+1][tempx] = [tempy,tempx]
            visited[tempy+1,tempx] = nodes[tempy+1][tempx]
            if int(info[tempy+1][tempx]) + nodes[tempy][tempx] < closest or closest == -1:
                closest = int(info[tempy+1][tempx]) + nodes[tempy][tempx]
    if tempx > 0:
        #check left node
        if int(info[tempy][tempx-1]) + nodes[tempy][tempx] < nodes[tempy][tempx-1] or nodes[tempy][tempx-1] == -1:
            nodes[tempy][tempx-1] = int(info[tempy][tempx-1]) + nodes[tempy][tempx]
            parent[tempy][tempx-1] = [tempy,tempx]
            visited[tempy,tempx-1] = nodes[tempy][tempx-1]
            if int(info[tempy][tempx-1]) + nodes[tempy][tempx] < closest or closest == -1:
                closest = int(info[tempy][tempx-1]) + nodes[tempy][tempx]
    if tempy > 0:
        #check node above
        if int(info[tempy-1][tempx]) + nodes[tempy][tempx] < nodes[tempy-1][tempx] or nodes[tempy-1][tempx] == -1:
            nodes[tempy-1][tempx] = int(info[tempy-1][tempx]) + nodes[tempy][tempx]
            parent[tempy-1][tempx] = [tempy,tempx]
            visited[tempy-1,tempx] = nodes[tempy-1][tempx]
            if int(info[tempy-1][tempx]) + nodes[tempy][tempx] < closest or closest == -1:
                closest = int(info[tempy-1][tempx]) + nodes[tempy][tempx]
                
    

#main
nodes[0][0] = int(info[0][0]) 
currentx = 0
currenty = 0
#updateSurroundings(0,0)
#coord = [0,0]
while nodes[yval-1][xval-1] == -1:    
    updateSurroundings(currenty,currentx)    
    currenty = min(visited, key=visited.get)[0]
    currentx = min(visited, key=visited.get)[1]
    del visited[currenty,currentx]
    """
    print nodes[0]
    print nodes[1]
    print nodes[2]
    print nodes[3]
    print nodes[4]
    print " "
    """
print nodes[yval-1][xval-1]
"""
print " "
print " "
print parent[0]
print parent[1]
print parent[2]
print parent[3]
#print parent[4]

print " "
print nodes[0]
print nodes[1]
print nodes[2]
print nodes[3]
print nodes[4]
"""
