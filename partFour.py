import copy
############################################################
# DP used
# runs in time O(N) where N is number of nodes(r*c)
############################################################
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
############################################################
# visited is a dictionary of [r,c]:distance
# info are the distance values for each node
# nodes are the current values, with -1 being unvisited
# parent keeps track of the parent node of the position that is being occupied
############################################################


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
############################################################
# Updates path from current nodes to surrounding nodes.
# If less than current val or surrounding node is unvisited,
# surrounding node is updated. 
############################################################

def test():
    print ""
    for x in range(yval):
        print nodes[x]
        


nodes[0][0] = int(info[0][0]) 
currentx = 0
currenty = 0
while nodes[yval-1][xval-1] == -1:    
    updateSurroundings(currenty,currentx)    
    currenty = min(visited, key=visited.get)[0]
    currentx = min(visited, key=visited.get)[1]
    del visited[currenty,currentx]
    #test()
print nodes[yval-1][xval-1]
############################################################  
# starts updating surrounding nodes at position (0,0)
# chooses next node to update based on smallest value in
# dictionary, and finishes when the current node is (r,c)
# uncomment #test() to see the map updating
############################################################  

