lines = list(map(int, open("data1.in").readlines()))

for num1 in lines:
    if (2020 - num1) in lines:
        print(num1 * (2020 - num1))
        break

# part 2
for num1 in lines:
    for num2 in lines:
        if (2020 - num2 - num1) in lines:
            print(num1 * num2 * (2020 - num1 - num2))
            break

# short solutuions
next(print(x * (2020 - x)) for x in lines if 2020 - x in lines)
next(
    print(x * y * (2020 - x - y)) for x in lines for y in lines if 2020 - y - x in lines
)
