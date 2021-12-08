with open("2021/data08.in", "r") as f:
    lines = f.read().splitlines()


# part 1
output_values = [x.split(" | ")[1].split(" ") for x in lines]
output_values = [item for sublist in output_values for item in sublist]
lengths = [2, 3, 4, 7]
print(sum(len(x) == i for i in lengths for x in output_values))

# part 2
def common(a, b):
    return len(set(a).intersection(b))


result = 0
for x in lines:
    input_values, output_values = x.split(" | ")
    input_values = ["".join(sorted(x, key=str.lower)) for x in input_values.split(" ")]
    output_values = [
        "".join(sorted(x, key=str.lower)) for x in output_values.split(" ")
    ]

    dic = {}
    for x in input_values:
        if len(x) == 2:
            dic[1] = x
        elif len(x) == 4:
            dic[4] = x
        elif len(x) == 3:
            dic[7] = x
        elif len(x) == 7:
            dic[8] = x

    for x in input_values:
        if x not in list(dic.values()):
            if len(x) == 6 and common(x, dic.get(1, "")) == 1:
                dic[6] = x
            elif len(x) == 5 and common(x, dic.get(1, "")) == 2:
                dic[3] = x

    for x in input_values:
        if x not in list(dic.values()):
            if len(x) == 5:
                if common(x, dic.get(6, "")) == 5:
                    dic[5] = x
                elif common(x, dic.get(6, "")) == 4:
                    dic[2] = x
            elif len(x) == 6 and common(x, dic.get(1, "")) == 2:
                if common(x, dic.get(3, "")) == 4:
                    dic[0] = x
                elif common(x, dic.get(3, "")) == 5:
                    dic[9] = x

    result += int(
        "".join([str(k) for x in output_values for k, v in dic.items() if v == x])
    )
print(result)