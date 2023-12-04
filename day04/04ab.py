from collections import defaultdict
file1 = open('./day04/input.txt', 'r') 
#file1 = open('./day04/example.txt', 'r') 
Lines = [l.strip() for l in file1.readlines()]

result=0
M = defaultdict(int)
for i,l in enumerate(Lines):
    M[i]+=1
    _,data = l.split(":")
    winning, youhave = data.split(" | ")
    win=[int(x) for x in winning.strip().split()]
    you=[int(x) for x in youhave.strip().split()]
    merge=set(win) & set(you)
    hits=len(merge)
    if hits>0:
        result+=2**(hits-1)
    for j in range(hits):
        M[i+1+j]+=M[i]

print(result)
print(sum(M.values()))