import re
import copy

with open("2022/day05.input", "r") as f:
    lines = f.read().splitlines()

numberOfLinesStartingStack = 10
startingStack = lines[: numberOfLinesStartingStack - 2]
procedureRaw = lines[numberOfLinesStartingStack:]

procedure = [list(map(int, re.findall(r"(\d+)", x))) for x in procedureRaw]

crates9000 = []
for i in range(1, len(startingStack[0]) + 1, 4):
    crates9000.append([x[i] for x in startingStack if x[i] != " "])
crates9001 = copy.deepcopy(crates9000)

for move, fromCrate, toCrate in procedure:

    for moves in range(move):
        crates9000[toCrate - 1].insert(0, crates9000[fromCrate - 1][0])
        crates9000[fromCrate - 1] = crates9000[fromCrate - 1][1:]

    crates9001[toCrate - 1][:0] = crates9001[fromCrate - 1][0:move]
    crates9001[fromCrate - 1] = crates9001[fromCrate - 1][move:]

print(f"""9000: {"".join(x[0] for x in crates9000)}""")
print(f"""9001: {"".join(x[0] for x in crates9001)}""")
