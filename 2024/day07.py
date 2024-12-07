import itertools

with open("2024/day07.input", "r") as f:
    lines = f.read().splitlines()

example = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".split(
    "\n"
)

operatorsDict2 = {}
operatorsDict3 = {}


def CorrectEquation(testValue, numbers, operatorTypes, operatorsdict):
    numbersLength = len(numbers)
    dicta = globals()[operatorsdict]

    if numbersLength not in dicta:
        dicta[numbersLength] = list(
            itertools.product(operatorTypes, repeat=numbersLength - 1)
        )

    for operators in dicta[numbersLength]:
        # print(operators)
        result = numbers[0]

        for index, number in enumerate(numbers[1:]):
            operator = operators[index]
            if operator == "||":
                result = eval(f"{result}{number}")
            else:
                result = eval(f"{result}{operator}{number}")

        if result == testValue:
            return True
    return False


sum = 0
sum2 = 0
for index, equation in enumerate(lines):
    split = equation.split(": ")
    testValue = int(split[0])
    numbers = split[1].split(" ")

    if CorrectEquation(testValue, numbers, ["*", "+"], "operatorsDict2"):
        sum += testValue
    if CorrectEquation(testValue, numbers, ["*", "+", "||"], "operatorsDict3"):
        sum2 += testValue
print(sum)
print(sum2)
