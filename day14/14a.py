file1 = open('./day14/input.txt', 'r') 
#file1 = open('./day14/example.txt', 'r') 
Lines = [l.strip() for l in file1.readlines()]

M= [[c for c in l.strip()] for l in Lines]

maxX=len(M[0])
maxY=len(M)

for x in range(maxX):
    for y in range(1,maxY):
        for z in range(y):
            if M[y-z][x]=='O' and y-z>0 and M[y-z-1][x]=='.':
                M[y-z][x]='.'
                M[y-z-1][x]='O'
            else:
                break 

result=0
for y in range(maxY):
    for x in range(maxX):
        if M[y][x]=='O':
            result+=maxY-y

print(result)