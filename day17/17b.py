import heapq
file1 = open('./day17/input.txt', 'r') 
#file1 = open('./day17/example.txt', 'r') 
Lines = [l.strip() for l in file1.readlines()]

M={}
for y, l in enumerate(Lines):
    for x, c in enumerate(l):
        M[(x,y)]=int(c)
maxY=y
maxX=x
#item = (cost,x,y,bx,by) bx,by banned direction
result=0
visited=set()
toVisit=[(0,0,0,0,0)]
while len(toVisit):
    cost,x,y,bx,by = heapq.heappop(toVisit)
    if (x,y)==(maxX,maxY):
        result=cost
        break
    if (x,y,bx,by) in visited:
        continue
    visited.add((x,y,bx,by))
    for dx,dy in [(0,-1),(1,0),(0,1),(-1,0)]:
        if (dx,dy)==(bx,by) or (dx,dy)==(-bx,-by):
            continue
        xaux,yaux,costaux=x,y,cost
        for d in range(1,11):
            xaux=xaux+dx
            yaux=yaux+dy
            if (xaux,yaux) in M :
                costaux+=M[(xaux,yaux)]
                if d >=4:
                    heapq.heappush(toVisit,(costaux,xaux,yaux,dx,dy))
print(result)  
print("hello")