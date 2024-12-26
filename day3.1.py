import re

file = open("day3.txt", "r")
string = file.read()

# Must put r"" prefix so that escape sequences arent read in
regex = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"
result = 0
do = True

# Findall returns an array of matches
for report in re.findall(regex, string):
    if report == "do()":
        do = True
    elif report == "don't()":
        do = False
    elif (report.startswith("mul") and do):  
        numbers = re.findall(r"\d{1,3}", report)
        result += (int(numbers[0]) * int(numbers[1]))

print(result)
    





