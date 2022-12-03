import numpy as np

with open("2021/data09.in", "r") as f:
    lines = f.read().splitlines()

numbers = [[int(y) for y in x] for x in lines]
numbers = np.array(numbers)
numbers = np.pad(numbers, pad_width=1, mode="constant", constant_values="10")

# part 1
res = 0
for i in range(1, len(numbers) - 1):
    for j in range(1, len(numbers[i]) - 1):
        if numbers[i][j] < min(
            numbers[i - 1][j], numbers[i + 1][j], numbers[i][j + 1], numbers[i][j - 1]
        ):
            res += numbers[i][j] + 1
print(res)
