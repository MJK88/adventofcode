with open("data15.in", "r") as f:
    lines = [int(x) for x in f.read().split(",")]
    lines2 = lines.copy()

# part 1
while len(lines) <= 2019:
    if lines.count(lines[-1]) == 1:
        lines.append(0)
    else:
        idx_turn = 1 + lines[-2::-1].index(lines[-1])
        lines.append(idx_turn)
print(lines[-1])

# part 2
dic = {x: i + 1 for i, x in enumerate(lines2)}
for i in range(len(lines2), 2020):
    if lines2[-1] in dic:
        next_number = i - dic[lines2[-1]]
        dic[lines2[-1]] = i
        lines2.append(next_number)
    else:
        dic[lines2[-1]] = i
        lines2.append(0)
print(lines2[-1])
