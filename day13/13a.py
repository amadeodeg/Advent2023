file1 = open('./day13/input.txt', 'r') 
#file1 = open('./day13/example.txt', 'r') 
blocks= file1.read().split("\n\n")

verticalResult=0
horizontalResult=0
for b in blocks:
    M= [[c for c in row.strip()] for row in b.split("\n")]
    maxX=len(M[0])
    maxY=len(M)
    #vertical
    for x in range(maxX-1):
        #print("--")
        simetry=True
        for i in range(x+1):
            leftIdx=x-i
            rightIdx=x+i+1
            if 0 <= leftIdx < rightIdx < maxX:
                #print(leftIdx,rightIdx)
                for j in range(maxY):
                    if M[j][leftIdx]!=M[j][rightIdx]:
                        simetry=False
                        break
                if not simetry:
                    break
        if simetry:
            verticalResult+=x+1
            break
    #horizontal   
    for y in range(maxY-1):
        #print("--")
        simetry=True
        for j in range(y+1):
            upIdx=y-j
            downIdx=y+j+1
            if 0 <= upIdx < downIdx < maxY:
                #print(upIdx,downIdx)
                for i in range(maxX):
                    if M[upIdx][i]!=M[downIdx][i]:
                        simetry=False
                        break
                if not simetry:
                    break
        if simetry:
            horizontalResult+=y+1
            break
    
print(verticalResult,horizontalResult)
print(verticalResult+100*horizontalResult)
print("hello")
