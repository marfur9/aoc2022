
inputfile = open('Day3/input.txt', 'r')
sum=0
letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
i=0
group=[]
for line in inputfile:
        
        if i<3:
                group.append(line)
                print(line + " added")
                i=i+1

        if i==3:
                member1,member2,member3=group[0],group[1],group[2]
                same=""
                for letter1 in member1:
                        for letter2 in member2:
                                for letter3 in member3:
                                        if letter1==letter2 and letter1==letter3:
                                                same=letter1
                                                print("found letter: " + letter1)
                                                break
                                else:
                                        continue
                                break
                        else:
                                continue
                        break
                
                for count, letter in enumerate(letters, start=1):
                        if same==letter:
                                sum=sum+count
                i=0
                group=[]

        
print (sum)