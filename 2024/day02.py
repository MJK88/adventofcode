with open("2024/day02.input", "r") as f:
    lines = f.read().splitlines()

example = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".split(
    "\n"
)


def isSafe(report):
    diffNeigbours = [report[x] - report[x + 1] for x in range(len(report) - 1)]
    return all(0 < x <= 3 for x in diffNeigbours) or all(
        0 > x >= -3 for x in diffNeigbours
    )


reports = [list(map(int, x.split(" "))) for x in lines]

print(sum(isSafe(report) for report in reports))

sumb = 0
for report in reports:
    for index in range(len(report)):
        if isSafe(report[:index] + report[index + 1 :]):
            sumb += 1
            break
print(sumb)
