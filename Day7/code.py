def updateSum(current, directories, size, parent):
        for directory in directories:
                if current == directory[0] and directory[2] == parent:
                        directory[1]=directory[1]+int(size)
                        return directories

        
        


def getSum(parent, directory, directories):
        for dir in directories:
                if directory == dir[0] and parent == dir[2]:
                        size=dir[1]
                        return size
        

def getParent(backstack):
        temp=backstack
        if len(backstack)<1:
                return ""
        else:
                temp.reverse()
                parent=temp[0]
                temp.reverse()

        return parent



inputfile = open('Day7/example.txt', 'r')
inputfile = open('Day7/input.txt', 'r')

#depth=0
directories=[]
backstack=[]
current=""
for line in inputfile:
        if len(line.split()) <3:
                
                if line.split()[0]=="$":
                        pass
                elif line.split()[0]=="dir":
                        pass
                else:
                        directories=updateSum(current, directories, line.split()[0], getParent(backstack))
        elif line.split()[2] == "..": #back
                previous=current
                current=backstack.pop()
                #depth=depth-1
                sumPrevious=getSum(current, previous, directories)
                directories=updateSum(current, directories, sumPrevious , getParent(backstack))
        elif line.split()[1] == "cd": #forward
                if current=="":
                        pass
                else:
                        
                        backstack.append(current)
                current=line.split()[2]

                directories.append([line.split()[2], 0, getParent(backstack)])
                #depth=depth+1
                



sum=0
#print(directories)
for directory in directories:
        if directory[1] <= 100000:
                sum=sum+directory[1]
print(sum)