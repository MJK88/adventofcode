import re

with open("data4.in", "r") as f:
    lines = [x.replace("\n", " ") for x in f.read().split("\n\n")]

# part 1
necessary_fields = ("byr", "iyr", "eyr", "hgt", "ecl", "hcl", "pid")
print(sum([all(field in x for field in necessary_fields) for x in lines]))

# part 2
patterns = [
    r"hcl:#[0-9a-f]{6}\b",
    r"pid:[0-9]{9}\b",
    r"byr:(19[2-9][0-9]|200[0-2])\b",
    r"ecl:(amb|blu|brn|gry|grn|hzl|oth)\b",
    r"iyr:(201[0-9]|2020)\b",
    r"eyr:(202[0-9]|2030)\b",
    r"hgt:(1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in)\b",
]

count = 0
for x in lines:
    if all(field in x for field in necessary_fields):
        valid = sum([bool(re.search(pattern, x)) for pattern in patterns])
        if valid == len(patterns):
            count += 1
print(count)
