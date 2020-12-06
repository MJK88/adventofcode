with open("data6.in", "r") as f:
    lines = [x.replace("\n", " ") for x in f.read().split("\n\n")]

# part 1
print(sum([len(set(x.replace(" ", ""))) for x in lines]))

# part 2
count = 0
for x in lines:
    x = x.split()
    for y in x[0]:
        if all(y in z for z in x[1:]):
            count += 1
print(count)