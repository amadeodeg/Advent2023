
from math import gcd
file1 = open('./day08/input.txt', 'r') 
#file1 = open('./day08/example.txt', 'r') 
instructions,myInput=file1.read().split("\n\n")

GOTO={"L":{}, "R":{}}
for line in myInput.splitlines():
    k, valLR = line.split(" = ")
    left, right = valLR[1:-1].split(", ")
    GOTO["L"][k]=left
    GOTO["R"][k]=right

maxIndex=len(instructions)

current=[]

for k in GOTO["L"]:
   if k[-1] == "A":
     current.append(k) 
results=[]     
time=0
indexInstruction=0
while True:
  time+=1
  for i, c in enumerate(current):
    current[i]=GOTO[instructions[indexInstruction]][current[i]]
    if current[i][-1] =="Z":
       results.append(time)
  if len(results)==len(current):
     break    
  indexInstruction=(indexInstruction+1)%maxIndex

def lcm(xs):
  ans = 1
  for x in xs:
    ans = (x*ans)//gcd(x,ans)
  return ans

print(lcm(results))
