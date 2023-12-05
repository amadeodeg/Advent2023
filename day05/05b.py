from collections import defaultdict
file1 = open('./day05/input.txt', 'r') 
#file1 = open('./day05/example.txt', 'r') 
#Lines = [l.strip() for l in file1.readlines()]
myInput=file1.read().split("\n\n")
seeds=[int(x) for x in myInput[0].split(":")[1].split()]
seedsRanges=[(seeds[i],seeds[i]+seeds[i+1]) for i in range(0,len(seeds),2)]
for i in range(1,len(myInput)):
    myRanges=[]
    for l in myInput[i].splitlines()[1:]:
        r=[int(x) for x in l.split()]
        myRanges.append(r)
    newSeeds=[]
    while len(seedsRanges)>0:
        checkSeed=False
        seedStar,seedEnd = seedsRanges.pop()
        for r in myRanges:
            destStart=r[0]
            sourStart=r[1]
            rangeLeng=r[2]
            ovini=max(seedStar,sourStart)
            ovend=min(seedEnd,sourStart+rangeLeng)
            if ovini < ovend: # overlap > 0
                newSeeds.append((destStart+(ovini-sourStart),destStart+(ovend-sourStart)))
                if seedStar < ovini:
                    seedsRanges.append((seedStar,ovini))
                if seedEnd > ovend:
                    seedsRanges.append((ovend,seedEnd))
                checkSeed=True
                break
        if not checkSeed:
            newSeeds.append((seedStar,seedEnd))
    seedsRanges=newSeeds

print(min(seedsRanges)[0])
