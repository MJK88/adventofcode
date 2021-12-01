import re
from collections import defaultdict

with open("data21.in", "r") as f:
    lines = f.read().splitlines()

d = defaultdict(set)
for x in lines:
    if match := re.match(r"(.*)\s\(contains (.*)\)", x):
        for y in match.group(1).split(" "):
            for z in match.group(2).split(", "):
                d[y].add(z)

i = 0
for k, v in d.items():
    if len(v) != 8:
        for x in lines:
            i += x.count(k)
print(i)
# d = {
#     match.group(1): match.group(2).split(", ")
#     for x in lines
#     if (match := re.match(r"(.*)\s\(contains (.*)\)", x))
# }


allergens = set(el for x in d.values() for el in x)
# print(allergens)
