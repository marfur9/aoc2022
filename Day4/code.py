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
        if r1list.issubset(r2list) or r2list.issubset(r1list):
                sum=sum+1
print(sum)