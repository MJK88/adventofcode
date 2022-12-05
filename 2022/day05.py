import re
import copy

with open("2022/day05.input", "r") as f:
    lines = f.read().splitlines()

numberOfLinesStartingStack = 10
startingStack = lines[: numberOfLinesStartingStack - 2]
procedureRaw = lines[numberOfLinesStartingStack:]

procedure = []
for x in procedureRaw:
    y = re.findall(r"(\d+)", x)
    procedure.append([int(y[0]), int(y[1]) - 1, int(y[2]) - 1])

crates9000 = []
for i in range(1, len(startingStack[0]) + 1, 4):
    crates9000.append([x[i] for x in startingStack if x[i] != " "])
crates9001 = copy.deepcopy(crates9000)

for x in procedure:
    move = x[0]
    fromCrate = x[1]
    toCrate = x[2]

    for moves in range(move):
        crates9000[toCrate].insert(0, crates9000[fromCrate][0])
        crates9000[fromCrate] = crates9000[fromCrate][1:]

    crates9001[toCrate][:0] = crates9001[fromCrate][0:move]
    crates9001[fromCrate] = crates9001[fromCrate][move:]

print(f"""9000: {"".join(x[0] for x in crates9000)}""")
print(f"""9001: {"".join(x[0] for x in crates9001)}""")
