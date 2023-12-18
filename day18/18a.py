
file1 = open('./day18/input.txt', 'r') 
#file1 = open('./day18/example.txt', 'r') 
Lines = [l.strip() for l in file1.readlines()]

UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)
DIRECTIONS={"U":UP,"R":RIGHT,"D":DOWN,"L":LEFT}
x,y=0,0
edge=set()
edge.add((x,y))
for l in Lines:
    d,n,color=l.split()
    n=int(n)
    dx,dy = DIRECTIONS[d]
    for _ in range(n):
        x+=dx
        y+=dy
        edge.add((x,y))

x,y =min(edge)
toVisit=[(x+1,y+1)]
inside=set()
while len(toVisit):
    i,j = toVisit.pop()
    for dx,dy in DIRECTIONS.values():
        ii=i+dx
        jj=j+dy
        if (ii,jj) not in edge and (ii,jj) not in inside:
            toVisit.append((ii,jj))
            inside.add((ii,jj))
print(len(edge)+len(inside))



jj=[b for a,b in edge]
jmin=min(jj)
jmax=max(jj)
ii=[a for a,b in edge]
imin=min(ii)
imax=max(ii)
aux=""
for j in range(jmax-jmin+1):
    for i in range(imax-imin+1):
        if (i+imin,j+jmin) in edge:
            aux+="#"
        elif (i+imin,j+jmin) in inside:
            aux+="x"
        else:
            aux+="."
    aux+="\n"
file2 = open('./day18/out.txt', 'w')
file2.write(aux)
print("hello")