

file = open("day1.txt", "r")
string = file.read()



listAll = string.split()
listA = [int(i) for j, i in enumerate(listAll) if j % 2 != 0]
listB = [int(i) for j, i in enumerate(listAll) if j % 2 == 0]
listA.sort()
listB.sort()
sum = 0
for i, x in enumerate(listA):
    sum += abs(listB[i] - x)


print(sum)
