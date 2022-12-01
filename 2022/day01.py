with open("2022/day01.input", "r") as f:
    lines = [list(map(int, x.split("\n"))) for x in f.read().split("\n\n")]

sums = [sum(x) for x in lines]
sortedSums = sorted(sums, reverse=True)

print(sortedSums[0], sum(sortedSums[:3]))
