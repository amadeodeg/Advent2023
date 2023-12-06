import math
file1 = open('./day06/input.txt', 'r') 
#file1 = open('./day06/example.txt', 'r') 
Lines = [l.strip() for l in file1.readlines()]
times=[int(x) for x in Lines[0].split(":")[1].split()]
distances=[int(x) for x in Lines[1].split(":")[1].split()]

result=1
for i in range(len(times)):
    t=times[i]
    d=distances[i]
    sq= math.sqrt(t*t-4*d)
    result*=math.ceil(sq)
print(result)

time=int(''.join(str(x)for x in times))
distance=int(''.join(str(x)for x in distances))
print(math.ceil(math.sqrt(time*time-4*distance)))