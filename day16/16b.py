file1 = open('./day16/input.txt', 'r') 
#file1 = open('./day16/example.txt', 'r') 
Lines = [l.strip() for l in file1.readlines()]

M=[[c for c in l]for l in Lines]
maxX=len(M[0])
maxY=len(M)

UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)
DIRECTIONS=[UP,RIGHT,DOWN,LEFT]
MIR1={UP:RIGHT, RIGHT:UP, DOWN:LEFT, LEFT:DOWN} # /
MIR2={UP:LEFT, RIGHT:DOWN, DOWN:RIGHT, LEFT:UP} # \
def nextTile(x,y,d):
    return (x+d[0],y+d[1],d)

def myFun(sx,sy,sd):
    current=[(sx,sy,sd)]
    visited=set()
    visited2=set()
    while len(current)>0:
        newCurrent=[]
        for (x,y,d) in current:
            if 0<=x<maxX and 0<=y<maxY:
                visited.add((x,y))
                if (x,y,d) in visited2:
                    continue
                visited2.add((x,y,d))
                c=M[y][x]
                if c==".":
                    newCurrent.append(nextTile(x,y,d))
                elif c=="/":
                    newCurrent.append(nextTile(x,y,MIR1[d]))
                elif c=="\\":
                    newCurrent.append(nextTile(x,y,MIR2[d]))
                elif c=="|":
                    if d==RIGHT or d==LEFT:
                        newCurrent.append(nextTile(x,y,UP))
                        newCurrent.append(nextTile(x,y,DOWN))
                    else:
                        newCurrent.append(nextTile(x,y,d))  
                elif c=="-":
                    if d==UP or d==DOWN:
                        newCurrent.append(nextTile(x,y,RIGHT))
                        newCurrent.append(nextTile(x,y,LEFT))
                    else:
                        newCurrent.append(nextTile(x,y,d))
        current=newCurrent
    return(len(visited))
result=0
for x in range(maxX):
    result=max(result,myFun(x,0,DOWN))
    result=max(result,myFun(x,maxY-1,DOWN))
for y in range(maxY):
    result=max(result,myFun(0,y,RIGHT))
    result=max(result,myFun(maxX-1,y,LEFT))
print(result)