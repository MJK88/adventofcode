with open("data02.in", "r") as f:
    lines = f.read().splitlines()

h = 0
d = 0
a = 0
for x in lines:
    x = x.split(" ")

    if x[0].startswith("f"):
        h += int(x[1])
        d += a * int(x[1])
    elif x[0].startswith("d"):
        a += int(x[1])
    elif x[0].startswith("u"):
        a -= int(x[1])

print(h, d, h * d)
