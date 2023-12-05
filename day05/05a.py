from collections import defaultdict
file1 = open('./day05/input.txt', 'r') 
#file1 = open('./day05/example.txt', 'r') 
#Lines = [l.strip() for l in file1.readlines()]
myInput=file1.read().split("\n\n")
seeds=[int(x) for x in myInput[0].split(":")[1].split()]

SEEDS = defaultdict(int)
SEEDS[1]=seeds
for i in range(1,len(myInput)):
    myRanges=[]
    for l in myInput[i].splitlines()[1:]:
        r=[int(x) for x in l.split()]
        myRanges.append(r)
    newSeeds=[]
    for s in SEEDS[i]:
        checkSeed=False
        for r in myRanges:
            destStart=r[0]
            sourStart=r[1]
            rangeLeng=r[2]
            if sourStart <= s < sourStart+rangeLeng:
                newSeeds.append(destStart+(s-sourStart))
                checkSeed=True
                break
        if not checkSeed:
            newSeeds.append(s)
    SEEDS[i+1]=newSeeds

print(min(SEEDS[i+1]))
