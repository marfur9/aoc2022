containers=[]
numContainers = 9
inputfile = open('Day5/test.txt', 'r')
#inputfile = open('Day5/input.txt', 'r')

for i in range(0,numContainers,1):
    containers.append([])

for line in inputfile:
    for i in range(1,1+(numContainers*4),4):
        print(line[i])
        if line[i] == " ":
            pass
        elif i == 1:
            containers[0].append(line[i])
        else:
            containers[int((i-1)/4)].append(line[i])
print(containers)
    