import sys

def checkPangram(givenPangram):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]

    pangramCount = 0
    missingList = []

    for i in range(26):
        if alphabet[i] in givenPangram.lower():
            pangramCount = pangramCount + 1
        else:
            missingList.append(alphabet[i])
            
            

        
    if pangramCount == 26:
        return "pangram"
    else:
        return ("missing " + str(missingList)).replace(", ","").replace("[","").replace("]","").replace("'","")

sets = {}

setInput = sys.stdin
for h in setInput:
    setNum = h

for k in range(1, setNum):
    sets["{0}".format(k)] = sys.stdin

for m in setNum:
    print(abs(checkPangram(sets[str(int(m) + 1)])))
