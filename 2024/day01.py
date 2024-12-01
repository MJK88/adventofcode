with open("2024/day01.input", "r") as f:
    lines = f.read().splitlines()

example = """3   4
4   3
2   5
1   3
3   9
3   3""".split(
    "\n"
)

lista = [x.split("   ") for x in lines]
trasnposedList = list(map(list, zip(*lista)))
sortedList = [sorted(x) for x in trasnposedList]

totalDistance = 0
for i in range(len(sortedList[0])):
    totalDistance += abs(int(sortedList[0][i]) - int(sortedList[1][i]))
print(totalDistance)

similarityScore = 0
for x in sortedList[0]:
    similarityScore += int(x) * sortedList[1].count(x)
print(similarityScore)
