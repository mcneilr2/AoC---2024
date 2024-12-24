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

def safetyCheck(report):
    up = None
    for i in range(len(report)-1):
        score = report[i] - report[i+1]
        if score > 3 or score < -3 or score == 0:
            return False
        if score < 0 and up == True:
            return False
        if score > 0 and up == False:
            return False
        
        if score < 0:
            up = False
        else: up = True

    return True

safeReports = 0
for report in numsArray:
    if safetyCheck(report):
        safeReports += 1
    else:
        for i, level in enumerate(report):
            alteredReport = report.copy()
            alteredReport.pop(i)
            if safetyCheck(alteredReport):
                safeReports += 1
                break
    
print(safeReports)




