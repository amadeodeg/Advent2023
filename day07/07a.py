from collections import Counter
file1 = open('./day07/input.txt', 'r') 
#file1 = open('./day07/example.txt', 'r') 
Lines = [l.strip() for l in file1.readlines()]

def getN(x):
    if x.isdigit():
        return int(x)
    d={'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return d[x]

handList=[]
for l in Lines:
    myHand, bid = l.split()
    myHand=[getN(x) for x in myHand]
    bid=int(bid)
    handList.append((myHand,bid))
 
def power(hand):
    c = Counter(hand[0])
    val=sorted(c.values())
    if val == [1,1,1,1,1]:
        return 1
    if val == [1,1,1,2]:
        return 2
    if val == [1,2,2]:
        return 3
    if val == [1,1,3]:
        return 4
    if val == [2,3]:
        return 5
    if val == [1,4]:
        return 6
    if val == [5]:
        return 7
    
handListSorted = sorted(handList, key=lambda x:(power(x),x))   
result=0
for i,hand in enumerate(handListSorted):
    result+=(i+1)*hand[1]
    
print(result)