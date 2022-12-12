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

lcmPart2 = math.lcm(*[int(instruction[2]) for instruction in instructions])


def MonkeyBusiness(rounds, relief):
    monkeyStats = {}
    for roundNumber in range(rounds):
        for i, monkey in enumerate(worryLevels):
            for old in monkey:
                if i not in monkeyStats:
                    monkeyStats[i] = 1
                else:
                    monkeyStats[i] = monkeyStats[i] + 1

                if instructions[i][1] == "old":
                    new = eval(old + instructions[i][0] + old)
                else:
                    new = eval(old + instructions[i][0] + instructions[i][1])

                new = eval(str(new) + relief)

                if new % int(instructions[i][2]) == 0:
                    worryLevels[int(instructions[i][3])].append(str(new))
                else:
                    worryLevels[int(instructions[i][4])].append(str(new))
                worryLevels[i] = worryLevels[i][1:]

    return math.prod(sorted(set(monkeyStats.values()))[-2:])


print(MonkeyBusiness(20, "//3"))
print(MonkeyBusiness(10000, "%lcmPart2"))
