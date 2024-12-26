import re

file = open("day3.txt", "r")
string = file.read()

regex = r"mul\(\d{1,3},\d{1,3}\)"
result = 0
for report in re.findall(regex, string):
    numbers = re.findall(r"\d{1,3}", report)
    result += (int(numbers[0]) * int(numbers[1]))

print(result)