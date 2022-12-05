#inputfile = open('Day4/example.txt', 'r')
inputfile = open('Day4/input.txt', 'r')
sum=0
for line in inputfile:
        range1=line.split(",")[0]
        range1from=range1.split("-")[0]
        range1to=range1.split("-")[1]
        range2=line.split(",")[1]
        range2from=range2.split("-")[0]
        range2to=range2.split("-")[1]
        r1list=set([*range(int(range1from),int(range1to)+1)])
        r2list=set([*range(int(range2from),int(range2to)+1)])
        for section1 in r1list:
                for section2 in r2list:
                        if section1==section2:
                                sum=sum+1
                                break
                else:
                        continue
                break
print(sum)