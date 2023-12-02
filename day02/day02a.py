file1 = open('./day02/input.txt', 'r') 
Lines = [l.strip() for l in file1.readlines()]

R=12
G=13
B=14

result=0
for l in Lines:
    [g,sets] = l.split(":")
    gameNumber = int(g.split(" ")[1])
    plays = sets.split(";")
    checkvar=True
    for p in plays:
        rgbtry=p.split(",")
        for a in rgbtry:
            [n,color]=a.strip().split(" ")
            c=color[0]
            n=int(n)
            if (c=="r" and n>R) or (c=="g" and n>G) or (c=="b" and n>B):
                checkvar=False
    if checkvar:
        result+=gameNumber
print(result)
print("hello")