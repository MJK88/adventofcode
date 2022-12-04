with open("2022/day04.input", "r") as f:
    lines = f.read().splitlines()

numberFullyContains = 0
numberPairsOverlap = 0
for x in lines:
    first, second = x.split(",")
    firstRange = range(int(first.split("-")[0]), int(first.split("-")[1]) + 1)
    secondRange = range(int(second.split("-")[0]), int(second.split("-")[1]) + 1)

    if set(firstRange).issubset(secondRange) or set(secondRange).issubset(firstRange):
        numberFullyContains += 1
    if bool(set(firstRange) & set(secondRange)):
        numberPairsOverlap += 1
print(numberFullyContains, numberPairsOverlap)
