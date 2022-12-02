# rock = 1      4       7
# paper = 2     5       8
# scissors = 3     6       9


def rps(enemy, outcome):
        score = 0
        if enemy == "A":
                if outcome == "X":
                        score=3
                elif outcome == "Y":
                        score=4
                elif outcome == "Z":
                        score=8
        elif enemy== "B":
                if outcome =="X":
                        score=1
                elif outcome == "Y":
                        score=5
                elif outcome == "Z":
                        score=9
        elif enemy== "C":
                if outcome =="X":
                        score=2
                elif outcome == "Y":
                        score=6
                elif outcome == "Z":
                        score=7
        return score
        

score=0
inputfile = open('Day2/input.txt', 'r')
for line in inputfile:
        moves=line.split()
        enemy=moves[0]
        outcome=moves[1]
        score= score+rps(enemy, outcome)
print("Score: " + str(score))