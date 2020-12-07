import re

with open("data7.in", "r") as f:
    lines = f.read().splitlines()


def search(listofrules, color):
    colors = []
    for x in listofrules:
        match = re.search(rf"(.*) bags contain .* {color} bag", x)
        if match and match.group(1) not in colors:
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