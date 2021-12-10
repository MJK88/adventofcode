with open("2021/data10.in", "r") as f:
    lines = f.read().splitlines()

points = {")": 3, "]": 57, "}": 1197, ">": 25137}
points2 = {")": 1, "]": 2, "}": 3, ">": 4}
couples = {"{": "}", "[": "]", "(": ")", "<": ">"}

part1_result = 0
part2_results = []

for x in lines:
    corrupt = False
    expectation = []

    for char in x:
        if char in couples.keys():
            expectation.append(char)
        if char in couples.values():
            if couples[expectation[-1]] == char:
                expectation.pop(-1)
            else:
                part1_result += points[char]
                corrupt = True
                break

    if not corrupt:
        part2_sum = 0
        for y in [couples[i] for i in expectation[::-1]]:
            part2_sum *= 5
            part2_sum += points2[y]
        part2_results.append(part2_sum)

print(
    f"Answer part 1: {part1_result}, Answer part 2: {sorted(part2_results)[len(part2_results) // 2]}"
)
