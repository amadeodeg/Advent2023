file1 = open('./day03/input.txt', 'r') 
#file1 = open('./day03/example.txt', 'r') 
Lines = [l.strip() for l in file1.readlines()]
M = [[c for c in l] for l in Lines]
maxR=len(M)
maxC=len(M[0])

def checkSymbol(row, col):
    for rr in [-1,0,1]:
        for cc in [-1,0,1]:
            if 0<row+rr<maxR and 0<col+cc<maxC:
                ch=M[row+rr][col+cc]
                if not ch.isdigit() and ch!='.':
                    return True                
    return False

result=0
myNumber=0
hasSymbol=False
for row in range(maxR):
    for col in range(maxC):
        myChar = M[row][col]
        if myChar.isdigit():
            myNumber=myNumber*10+int(myChar)
            hasSymbol=hasSymbol or checkSymbol(row,col)
        if col==maxC-1 or not myChar.isdigit():
            if hasSymbol:
                result+=myNumber
            myNumber=0
            hasSymbol=False

print(result)
        
        
        

    