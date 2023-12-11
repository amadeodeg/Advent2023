file1 = open('./day10/input.txt', 'r') 
#file1 = open('./day10/example.txt', 'r') 
Lines = [l.strip() for l in file1.readlines()]

UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)

OPTIONS={
    '|': [UP, DOWN],
    '-': [LEFT, RIGHT],
    'L': [UP, RIGHT],
    'J': [LEFT, UP],
    '7': [LEFT, DOWN],
    'F': [RIGHT, DOWN],
    '.': [],
    'S': [],
}
M={}
sx,sy = -1,-1
for y, line in enumerate(Lines):
    for x, charact in enumerate(line):
        aux=[]
        for dx,dy in OPTIONS[charact]:
            aux.append((x+dx,y+dy))
        M[(x,y)]=aux
        if charact == 'S':
            sx=x
            sy=y
startPos=(sx,sy)
aux=[]
for dx,dy in [UP,DOWN,LEFT,RIGHT]:
    if startPos in M.get((sx+dx,sy+dy),[]):
        aux.append((sx+dx,sy+dy))
M[startPos]=aux

path=[]
path.append(startPos)
myNext = M[startPos][0]
while myNext!=startPos:
    path.append(myNext)
    for i in M[myNext]:
        if i != path[-2]:
            myNext=i
print(len(path)/2)