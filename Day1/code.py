def compareToBiggest(biggest, current):
    if biggest >= current:
        return biggest
    else:
        return current

biggest=0
current=0
inputfile = open('Day1/input.txt', 'r')

for line in inputfile:
    if line.strip(): #not empty
        current=current+int(line)
    else: #empty
        biggest=compareToBiggest(biggest, current)
        current=0

print(biggest)
