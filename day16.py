import re
from collections import defaultdict
from math import prod

with open("data16.in", "r") as f:
    lines = f.read().splitlines()

valid = set()
for x in lines:
    if x.startswith("your"):
        break
    if match := re.match(r".*: (\d+)-(\d+) or (\d+)-(\d+)", x):
        for i, j in [(1, 2), (3, 4)]:
            valid.update(
                [x for x in range(int(match.group(i)), int(match.group(j)) + 1)]
            )

tickets_idx = lines.index("nearby tickets:") + 1
print(
    sum(
        [
            y
            for x in lines[tickets_idx:]
            for y in map(int, x.split(","))
            if y not in valid
        ]
    )
)

# part 2
# get valid tickets
tickets = []
for x in lines[tickets_idx:]:
    if all(y in valid for y in map(int, x.split(","))):
        tickets.append(list(map(int, x.split(","))))

# get departure valid ranges as a dict
ticket_fields = {}
for x in lines:
    if match := re.match(r"(.*): (\d+)-(\d+) or (\d+)-(\d+)", x):
        valid = set()
        for i, j in [(2, 3), (4, 5)]:
            valid.update(
                [x for x in range(int(match.group(i)), int(match.group(j)) + 1)]
            )
        ticket_fields[match.group(1)] = valid

# find which field is any of the ranges
field_idx = defaultdict(list)
for name, valid_range in ticket_fields.items():
    for i in range(len(tickets[0])):
        temp_list = [x[i] for x in tickets]
        if all(y in valid_range for y in temp_list):
            field_idx[name].append(i)

# remove indices
real_idx = {}
while True:
    remove_idx = []
    for name, index in field_idx.items():
        if len(index) == 1:
            real_idx[name] = index[0]
            remove_idx.append(index[0])
    for key in field_idx.keys():
        for values in remove_idx:
            if values in field_idx[key]:
                field_idx[key].remove(values)
    if len(real_idx.keys()) == len(field_idx.keys()):
        break

# get departure field of my ticket
my_ticket = list(map(int, lines[lines.index("your ticket:") + 1].split(",")))
print(prod([my_ticket[i] for name, i in real_idx.items() if "departure" in name]))
