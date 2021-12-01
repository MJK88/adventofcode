import re

with open("data14.in", "r") as f:
    lines = f.read().splitlines()

mem = {}
for x in lines:
    if x.startswith("mask"):
        mask = x.split(" = ")[1]
    elif match := re.match(r"mem\[(\d+)\] = (\d+)", x):
        result = f"{int(match.group(2)):0>36b}"
        result = [mask if mask != "X" else value for mask, value in zip(mask, result)]
        mem[match.group(1)] = int("".join(result), 2)

print(sum(x for x in mem.values()))


def convert_float(addr):
    if "X" not in addr:
        return [int(addr, 2)]
    x = convert_float(addr.replace("X", "0", 1))
    y = convert_float(addr.replace("X", "1", 1))
    return x + y


mem = {}
for x in lines:
    if x.startswith("mask"):
        mask = x.split(" = ")[1]
    elif match := re.match(r"mem\[(\d+)\] = (\d+)", x):
        address = f"{int(match.group(1)):0>36b}"
        floats = "".join(
            [mask if mask != "0" else char for mask, char in zip(mask, address)]
        )
        results = convert_float(floats)
        for el in results:
            mem[el] = int(match.group(2))

print(sum(x for x in mem.values()))
