def occurence(string):
    freq = {}

    for i in string:
        if i in freq:
            freq[i] = freq[i] + 1
        else:
            freq[i] = 1
    return (max(freq, key=freq.get), min(freq, key=freq.get))


def transpose_list(list_of_strings):
    return ["".join(x) for x in zip(*list_of_strings)]


# open file
with open("data03.in", "r") as f:
    lines = f.read().splitlines()

# part 1
gamma = epsilon = ""
lines_transposed = transpose_list(lines)
for x in lines_transposed:
    most, least = occurence(x)
    gamma += most
    epsilon += least

print(gamma, epsilon, int(gamma, 2) * int(epsilon, 2))

# part 2
oxygen = co = lines.copy()

for i in range(len(lines[0])):
    if len(oxygen) == 1:
        break
    lines_transposed = transpose_list(oxygen)
    most, least = occurence(lines_transposed[i])
    if most == least:
        oxygen = [x for x in oxygen if x[i] == "1"]
    else:
        oxygen = [x for x in oxygen if x[i] == most]

for i in range(len(lines[0])):
    if len(co) == 1:
        break
    lines_transposed = transpose_list(co)
    most, least = occurence(lines_transposed[i])
    if most == least:
        co = [x for x in co if x[i] == "0"]
    else:
        co = [x for x in co if x[i] == least]

print(oxygen, co, int(oxygen[0], 2) * int(co[0], 2))
