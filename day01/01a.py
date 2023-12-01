import re

file1 = open('./day01/input.txt', 'r') 
Lines = [l.strip() for l in file1.readlines()]

res = 0
for l in Lines:
    aa = re.sub("[^0-9]","",l)
    n = int(aa[0]+aa[-1])
    #print(n)
    res+=n

print(res)