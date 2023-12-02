file1 = open('./day02/input.txt', 'r') 
Lines = [l.strip() for l in file1.readlines()]

result=0
for l in Lines:
    [g,sets] = l.split(":")
    plays = sets.split(";")
    R=0
    G=0
    B=0
    for p in plays:
        rgbtry=p.split(",")
        for a in rgbtry:
            [n,color]=a.strip().split(" ")
            c=color[0]
            n=int(n)
            if c=="r":
                R=max(R,n)
            if c=="g":
                G=max(G,n)
            if c=="b":
                B=max(B,n)
    result+=(R*G*B)
print(result)