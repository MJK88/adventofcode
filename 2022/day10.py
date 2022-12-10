with open("2022/day10.input", "r") as f:
    lines = f.read().splitlines()

currentRegisterValue = 1
register = []
for x in lines:
    register.append(currentRegisterValue)
    if x.startswith("addx"):
        register.append(currentRegisterValue)
        currentRegisterValue += int(x.split(" ")[1])

print(sum([i * register[i - 1] for i in range(20, 221, 40)]))

pixels = [["." for i in range(40)] for j in range(6)]
for i in range(240):
    pixel = i % 40
    lineNumber = i // 40

    if register[i] - 1 <= pixel <= register[i] + 1:
        pixels[lineNumber][pixel] = "#"

for line in pixels:
    print("".join(line))
