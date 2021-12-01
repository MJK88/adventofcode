import re

with open("data7.in", "r") as f:
    lines = f.read().splitlines()

# part 1
def search(listofrules, color):
    colors = []
    for x in listofrules:
        match = re.search(rf"(.*) bags contain .* {color} bag", x)
        if match:
            colors.append(match.group(1))
    return colors


listofbags = search(lines, "shiny gold")
check = 0
numberofbags = len(listofbags)
while numberofbags != check:
    check = len(listofbags)
    for x in listofbags:
        for y in search(lines, x):
            if y not in listofbags:
                listofbags.append(y)
    numberofbags = len(listofbags)
print(len(listofbags))

# part 2
print(2 + 2 * (2 + 2 * (2 + 2 * (2 + 2 * (2 + 2 * (2 + 2 * (0)))))))
match = re.findall(rf"(?:{color} bags contain |, )(\d+) ([a-z]+ [a-z]+)", x)
print(lines[:10])
