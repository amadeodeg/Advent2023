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
        wrong=0
        for i in range(x+1):
            leftIdx=x-i
            rightIdx=x+i+1
            if 0 <= leftIdx < rightIdx < maxX:
                #print(leftIdx,rightIdx)
                for j in range(maxY):
                    if M[j][leftIdx]!=M[j][rightIdx]:
                        wrong+=1
        if wrong==1:
            verticalResult+=x+1
            break
    #horizontal   
    for y in range(maxY-1):
        #print("--")
        wrong=0
        for j in range(y+1):
            upIdx=y-j
            downIdx=y+j+1
            if 0 <= upIdx < downIdx < maxY:
                #print(upIdx,downIdx)
                for i in range(maxX):
                    if M[upIdx][i]!=M[downIdx][i]:
                        wrong+=1
        if wrong==1:
            horizontalResult+=y+1
            break
    
print(verticalResult+100*horizontalResult)

