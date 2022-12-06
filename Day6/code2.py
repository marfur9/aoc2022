def findDuplicates(chars):
        seen = set()


        for x in chars:
                if x in seen:
                        return False
                else:
                        seen.add(x)

        return True



inputfile = open('Day6/example.txt', 'r')
inputfile = open('Day6/input.txt', 'r')
for line in inputfile:
        chars=[]
        sum=0
        for char in line:
                sum=sum+1
                if len(chars) < 14:
                        chars.append(char)
                        if len(chars)==4:
                                if findDuplicates(chars):
                                        break
                else:
                        chars.reverse()
                        chars.pop()
                        chars.reverse()
                        chars.append(char)
                        if findDuplicates(chars):
                                break
        print(sum)