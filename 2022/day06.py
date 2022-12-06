with open("2022/day06.input", "r") as f:
    lines = f.read()


def DetectDistinctChars(string, number):
    for x in range(len(lines) - number + 1):
        if len(set(lines[x : x + number])) == number:
            return x + number


print(DetectDistinctChars(lines, 4), DetectDistinctChars(lines, 14))
