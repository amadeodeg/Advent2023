file1 = open('./day12/input.txt', 'r') 
#file1 = open('./day12/example.txt', 'r') 
Lines = [l.strip() for l in file1.readlines()]

def myCombinations(pattern, numbers):
    if not pattern:
        return len(numbers)==0
    if not numbers:
        return "#" not in pattern
    aux=0
    if pattern[0] in ".?":
        aux+= myCombinations(pattern[1:],numbers)
    if (
        pattern[0] in "#?"
        and numbers[0]<=len(pattern)
        and "." not in pattern[: numbers[0]]
        and (numbers[0] == len(pattern) or pattern[numbers[0]] != "#")
    ):
        aux+=myCombinations(pattern[numbers[0]+1 :],numbers[1:])
    return aux

result=0
for l in Lines:
    pattern, numbers =  l.split()
    numbers=[int(x) for x in numbers.split(",")]
    aux=myCombinations(pattern,numbers)
    print(pattern)
    print(numbers)
    result+=aux
print(result)