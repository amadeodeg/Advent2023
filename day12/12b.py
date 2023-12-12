file1 = open('./day12/input.txt', 'r') 
#file1 = open('./day12/example.txt', 'r') 
Lines = [l.strip() for l in file1.readlines()]
from functools import cache

@cache
def myCombinations(pattern, numbers):
    if not pattern:
        if len(numbers)==0:
            return 1
        return 0
    if not numbers:
        if "#" not in pattern:
            return 1
        return 0
    aux=0
    if pattern[0] in ".?":
        aux+= myCombinations(pattern[1:],numbers)
    if (
        pattern[0] in "#?"
        and 
        numbers[0]<=len(pattern)
        and 
        "." not in pattern[: numbers[0]]
        and 
        (numbers[0] == len(pattern) or pattern[numbers[0]] != "#")
    ):
        aux+=myCombinations(pattern[numbers[0]+1 :],numbers[1:])
    return aux

result=0
for l in Lines:
    pattern, numbers =  l.split()
    numbers=[int(x) for x in numbers.split(",")]
    pattern=((pattern+"?")*5)[0:-1]
    numbers=numbers*5
    aux=myCombinations(pattern,tuple(numbers))
    result+=aux
print(result)