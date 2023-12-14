file1 = open('./day14/input.txt', 'r') 
#file1 = open('./day14/example.txt', 'r') 
Lines = [l.strip() for l in file1.readlines()]
Matrix= [[c for c in l.strip()] for l in Lines]

maxX=len(Matrix[0])
maxY=len(Matrix)

def move(M):
    for x in range(maxX):
        for y in range(1,maxY):
            for z in range(y):
                if M[y-z][x]=='O' and y-z>0 and M[y-z-1][x]=='.':
                    M[y-z][x]='.'
                    M[y-z-1][x]='O'
                else:
                    break          
    return M

def myRotate(M): #clockwise stackoverflow
    return [list(reversed(col))for col in zip(*M)]

DB={}
a=0
while a < 10**9:
    a+=1
    #print(a)
    for _ in range(4):
        Matrix=move(Matrix)
        Matrix=myRotate(Matrix)
    MatrixSign=tuple(tuple(y) for y in Matrix)
    if MatrixSign in DB:
        cycleTime = a-DB[MatrixSign]
        aux=(10**9-a)//cycleTime
        a+=aux*cycleTime
    DB[MatrixSign]=a

result=0
for y in range(maxY):
    for x in range(maxX):
        if Matrix[y][x]=='O':
            result+=maxY-y
print(result)