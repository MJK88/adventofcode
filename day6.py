with open("data6.in", "r") as f:
    lines = [x.split("\n") for x in f.read().split("\n\n")]

# part 1
print(sum([len(set("".join(y))) for y in lines]))

# part 2
count = 0
for group in lines:
    for chars in group[0]:
        if all(chars in rest for rest in group[1:]):
            count += 1
print(count)

# short part 2
print(
    sum(
        [
            all(chars in rest for rest in group[1:])
            for group in lines
            for chars in group[0]
        ]
    )
)
