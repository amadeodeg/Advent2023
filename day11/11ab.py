from itertools import combinations
file1 = open('./day11/input.txt', 'r') 
#file1 = open('./day11/example.txt', 'r') 
Lines = [l.strip() for l in file1.readlines()]

galaxies=[]
for y, line in enumerate(Lines):
    for x, charact in enumerate(line):
        if charact== "#":
            galaxies.append((x,y))

emptyRowIdx=[]
for y, row in enumerate(Lines):
    if not "#" in row:
        emptyRowIdx.append(y)

emptyColIdx=[]
for x in range(len(Lines[0])):
    aux = [row[x] for row in Lines]
    if not "#" in aux:
        emptyColIdx.append(x)

def distance(a,b,offset):
    minx=min(a[0],b[0])
    maxx=max(a[0],b[0])
    miny=min(a[1],b[1])
    maxy=max(b[1],b[1])
    result=(maxx-minx)+(maxy-miny)
    result+=offset*len([i for i in emptyColIdx if i>minx and i<maxx])
    result+=offset*len([j for j in emptyRowIdx if j>miny and j<maxy])
    return result

distances=[]
for a,b in combinations(galaxies,2):
    distances.append(distance(a,b,1000000-1))

print(sum(distances))
