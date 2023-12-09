file1 = open('./day09/input.txt', 'r') 
#file1 = open('./day09/example.txt', 'r')
Lines = [l.strip() for l in file1.readlines()]

def checkAll(val):
    for v in val:
        if v!=0:
            return False
    return True

def calculateNext(numberList):
    aux=[]
    for i in range (len(numberList)-1):
        aux.append(numberList[i+1]-numberList[i])
    if checkAll(aux):
        return numberList[-1]
    else:
        return numberList[-1]+calculateNext(aux)

def calculatePrev(numberList):
    aux=[]
    for i in range (len(numberList)-1):
        aux.append(numberList[i+1]-numberList[i])
    if checkAll(aux):
        return numberList[0]
    else:
        return numberList[0]-calculatePrev(aux)    

resulta=0
resultb=0
for l in Lines:
    numberList=[int(x) for x in l.split()]
    a=calculateNext(numberList)
    resulta+=a
    b=calculatePrev(numberList)
    resultb+=b
print(resulta)
print(resultb)