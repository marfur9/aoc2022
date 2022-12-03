import time
start_time = time.time()

def splitstring(value):
    string1, string2 = value[:len(value)//2], value[len(value)//2:]
    return string1, string2

inputfile = open('Day3/example.txt', 'r')
sum=0
for line in inputfile:
        splitted=splitstring(line)
        comp1=splitted[0]
        comp2=splitted[1]
        same=""
        for item1 in comp1:
                for item2 in comp2:
                        if item1==item2:
                                same=item1
                                break
        letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        for count, letter in enumerate(letters, start=1):
                if same==letter:
                        sum=sum+count
                        break
print (sum)

print("Process finished --- %s seconds ---" % (time.time() - start_time))