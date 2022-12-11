import re
import math

with open("2022/day11.input", "r") as f:
    lines = f.read().split("\n\n")

regexWorryLevel = ".*items: (.*)\n"
monkeyInstructionsRegex = (
    ".*\n.*old ([^a-z]) (\d+|\w+).*\n.*divisible by (\d+).*\n.* (\d).*\n.*(\d)$"
)
worryLevels = [re.findall(regexWorryLevel, x)[0].split(", ") for x in lines]
instructions = [re.findall(monkeyInstructionsRegex, x)[0] for x in lines]

monkeyStats = {}
for rounds in range(20):
    for i, monkey in enumerate(worryLevels):
        for old in monkey:
            if i not in monkeyStats:
                monkeyStats[i] = 1
            else:
                monkeyStats[i] = monkeyStats[i] + 1

            if instructions[i][1] == "old":
                new = int(eval(old + instructions[i][0] + old))
            else:
                new = int(eval(old + instructions[i][0] + instructions[i][1]))
            new = new // 3
            # print(new)
            if new % int(instructions[i][2]) == 0:
                worryLevels[int(instructions[i][3])].append(str(new))
            else:
                worryLevels[int(instructions[i][4])].append(str(new))
            worryLevels[i] = worryLevels[i][1:]

print(worryLevels)
print(monkeyStats)
print(math.prod(sorted(set(monkeyStats.values()))[-2:]))
