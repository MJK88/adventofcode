with open("2021/data07.in", "r") as f:
    lines = f.read().splitlines()

lines = [int(x) for x in lines[0].split(",")]

# part 1
print(min([sum([abs(x - i) for x in lines]) for i in range(min(lines), max(lines))]))

# part 2 brute force


def fuel_consumption(origin, target):
    lis = range(abs(target - origin) + 1)
    total = 0
    for x in lis:
        total += x
    return total


print(
    min(
        [
            sum([fuel_consumption(x, i) for x in lines])
            for i in range(min(lines), max(lines))
        ]
    )
)
