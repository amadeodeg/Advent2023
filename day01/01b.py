import re

file1 = open('./day01/input.txt', 'r') 
Lines = [l.strip() for l in file1.readlines()]

res = 0
for l in Lines:
    digits=[]
    for i,c in enumerate(l):
        if c.isdigit():
            digits.append(int(c))
        for ii, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if l[i:].startswith(val):
                digits.append(ii+1)
    n = int(digits[0]*10+digits[-1])
    res+=n
    

print(res)