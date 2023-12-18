
file1 = open('./day18/input.txt', 'r') 
#file1 = open('./day18/example.txt', 'r') 
Lines = [l.strip() for l in file1.readlines()]

UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)
DIRECTIONS={"3":UP,"0":RIGHT,"1":DOWN,"2":LEFT}
x,y=0,0
corners=[]
corners.append((x,y))
edgeArea=0
for l in Lines:
    _,_,color=l.split()
    color=color[2:-1]
    n=int(color[:-1],16)
    dx,dy = DIRECTIONS[color[-1]]
    x+= dx*n
    y+= dy*n
    edgeArea+=n
    corners.append((x,y))
# https://en.m.wikipedia.org/wiki/Shoelace_formula
area=0
for i in range(len(corners)-1):
    x1,y1=corners[i]
    x2,y2=corners[i+1]
    aux= x1*y2 - x2*y1
    area+=aux
area=area//2
print(area+edgeArea//2+1)
print("hello")