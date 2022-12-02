def rps(enemy, me):
        score = 0
        if me == "X":
                if enemy == "A":
                        score=4
                elif enemy == "B":
                        score=1
                elif enemy == "C":
                        score=7
        elif me== "Y":
                if enemy =="A":
                        score=8
                elif enemy == "B":
                        score=5
                elif enemy == "C":
                        score=2
        elif me== "Z":
                if enemy =="A":
                        score=3
                elif enemy == "B":
                        score=9
                elif enemy == "C":
                        score=6
        return score
        

score=0
inputfile = open('Day2/input.txt', 'r')
for line in inputfile:
        moves=line.split()
        enemy=moves[0]
        me=moves[1]
        score= score+rps(enemy, me)
print("Score: " + str(score))