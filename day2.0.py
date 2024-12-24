file = open("day2.txt", "r")
string = file.read()
listAll = string.split("\n")

def arrayIfy(listAll):
    numsArray = []
    for x in listAll:
        nums = x.split()
        numArray = []
        for y in nums:
            numArray.append(int(y))
        numsArray.append(numArray)
    return numsArray

numsArray = arrayIfy(listAll)
safe = 0
for row in numsArray:
    dir = "unset"
    safety = True
    for i in range(0, len(row)-1):
        if (((row[i+1] - row[i]) > 0)):
            if(dir == "down" or ((row[i+1] - row[i]) > 3)):
                safety = False
            else: dir = "up"
        elif (((row[i+1] - row[i]) < 0)):
            if(dir == "up" or ((row[i+1] - row[i]) < -3)):
                safety = False
            else: dir = "down"
        elif(((row[i+1] - row[i]) == 0)):
            safety = False
        
        
    if safety: 
        safe += 1
        print("adding safety")
        
print(safe)

