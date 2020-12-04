import re

with open("data4.in", "r") as f:
    lines = [x.replace("\n", " ") for x in f.read().split("\n\n")]

# part 1
print(sum([x.count(":") == 8 or (x.count(":") == 7 and not "cid" in x) for x in lines]))

# part 2
patterns = [
    "hcl:#[0-9a-f]{6}",
    "pid:[0-9]{9}",
    "byr:(19[2-9][0-9]|200[0-2])",
    "ecl:(amb|blu|brn|gry|grn|hzl|oth)",
    "iyr:(20[1][0-9]|2020)",
    "eyr:(20[2][0-9]|2030)",
    "hgt:(1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in)",
]

count = 0
necessary_fields = ("byr", "iyr", "eyr", "hgt", "ecl", "hcl", "pid")
for x in lines:
    if all(field in x for field in necessary_fields):
        # if x.count(":") == 8 or (x.count(":") == 7 and not "cid" in x):
        valid = 0
        for pattern in patterns:
            if re.search(pattern, x):
                valid += 1
        if valid == len(patterns):
            count += 1
        # print(x, valid)
print(count)
