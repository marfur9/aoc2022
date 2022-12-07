inputfile = open('Day7/example.txt', 'r')
#inputfile = open('Day7/input.txt', 'r')

depth=0
directories=[]
for line in inputfile:
        if len(line.split()) <3:
                pass
        elif line.split()[2] == "..": #back
                depth=depth-1
        elif line.split()[1] == "cd":
                directories.append([line.split()[2], 0])
                depth=depth+1
        print (line.split()[1])