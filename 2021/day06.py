with open("2021/data06.in", "r") as f:
    lines = f.read().splitlines()

lines = [int(x) for x in lines[0].split(",")]

initial_state = lines.copy()

for day in range(80):
    new_fish = []

    for i, x in enumerate(lines):
        if x == 0:
            lines[i] = 6
            new_fish.append(8)
        else:
            lines[i] -= 1
    lines.extend(new_fish)

print(len(lines))

# part 2
fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i, x in enumerate(fish):
    fish[i] = initial_state.count(i)

for i in range(256):
    breed = fish.pop(0)
    fish.append(breed)
    fish[6] += breed

print(sum(fish))
