lines = list(map(int, open('data.in').readlines()))

next(print(x * (2020 - x)) for x in lines if 2020 - x in lines)
next(print(x * y * (2020 - x - y)) for x in lines for y in lines if 2020 - y - x in lines)
