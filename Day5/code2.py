def moveItem(containers, numToMove, fromContainer, toContainer):
        
        stackToMove=[]
        for i in range(0,int(numToMove),1):
                print(containers)
                stackToMove.append((containers[int(fromContainer)-1].pop()))
        stackToMove.reverse()
        for stack in stackToMove:
                containers[int(toContainer)-1].append(stack)
        
        
        
        return containers

inputfile = open('Day5/input.txt', 'r')
#inputfile = open('Day5/input.txt', 'r')
moves = []
numContainers = 0
for line in inputfile:
        if line.split()[0]=="1": # cargo numbers line
                
                containers=line.split()
                containers.reverse()
                numContainers=int(containers[0])
                break

containers=[]

for i in range(0,numContainers,1):
    containers.append([])
inputfile = open('Day5/input.txt', 'r')
#inputfile = open('Day5/input.txt', 'r')
for line in inputfile:
        if line.strip(): #non-empty line, do something
                if line.split()[0]=="move": #move line
                        moves.append(line.split())
                elif line.split()[0]=="1": # cargo numbers line
                        pass
                else: #cargo content line?
                        for i in range(1,1+(numContainers*4),4):
                                if line[i] == " ":
                                        pass
                                elif i == 1:
                                        containers[0].append(line[i])
                                else:
                                        containers[int((i-1)/4)].append(line[i])
        else: #empty line. do nothing
                pass


for container in containers:
        container.reverse()
for move in moves:
        containers=moveItem(containers, move[1], move[3], move[5])

result=""
for i in range(0, numContainers, 1):
        result=result+containers[i].pop()
print(result)
