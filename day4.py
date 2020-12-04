import re

with open("data4.in", "r") as f:
    lines = [x.replace("\n", " ") for x in f.read().split("\n\n")]

# part 1
print(sum([x.count(":") == 8 or (x.count(":") == 7 and not "cid" in x) for x in lines]))

# part 2
patterns = [
    r"hcl:#[0-9a-f]{6}",
    r"pid:[0-9]{9}\b",
    r"byr:(19[2-9][0-9]|200[0-2])",
    r"ecl:(amb|blu|brn|gry|grn|hzl|oth)",
    r"iyr:(201[0-9]|2020)",
    r"eyr:(202[0-9]|2030)",
    r"hgt:(1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in)",
]

count = 0
necessary_fields = ("byr", "iyr", "eyr", "hgt", "ecl", "hcl", "pid")
for x in lines:
    if all(field in x for field in necessary_fields):
        valid = 0
        for pattern in patterns:
            if re.search(pattern, x):
                valid += 1
        if valid == len(patterns):
            count += 1
print(count)
