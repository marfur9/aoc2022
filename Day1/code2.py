def compareToBiggest(biggest, current):
    for i in range(0,3,1):
        oldBiggest=biggest[i]
        if biggest[i] >= current:
            print("")
        else:
            biggest[i]=current
            print("biggest " + str(i) + " updated to " + str(current))
            biggest=compareToBiggest(biggest,oldBiggest)
            return biggest
    return biggest

biggest=[0,0,0]
current=0
inputfile = open('Day1/input.txt', 'r')

for line in inputfile:
    if line.strip(): #not empty
        current=current+int(line)
    else: #empty
        biggest=compareToBiggest(biggest, current)
        current=0


sum=0
for number in biggest:
    sum=sum+number

print(biggest)
print(sum)


#comment