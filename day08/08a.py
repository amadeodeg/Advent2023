
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
indexInstruction=0
current="AAA"
result=0
while current!="ZZZ":
  current=GOTO[instructions[indexInstruction]][current]
  indexInstruction=(indexInstruction+1)%maxIndex
  result+=1

print(result)