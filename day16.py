import re

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
departure = {}
for x in lines:
    if match := re.match(r"(departure.*): (\d+)-(\d+) or (\d+)-(\d+)", x):
        departure_valid = set()
        for i, j in [(2, 3), (4, 5)]:
            departure_valid.update(
                [x for x in range(int(match.group(i)), int(match.group(j)) + 1)]
            )
        departure[match.group(1)] = departure_valid

# find which field is any of the departure ranges
departure_idx = {}
for name, valid_range in departure.items():
    for i in range(len(tickets[0])):
        temp_list = [x[i] for x in tickets]
        if all(y in valid_range for y in temp_list):
            departure_idx[name] = i
print(departure_idx)
# get departure field of my ticket
my_ticket = lines[lines.index("your ticket:") + 1]