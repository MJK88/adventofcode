import string


def PositionAlphabet(char):
    return ord(char.lower()) - 96


def RockPaperScissors(one, two):
    choiceValue = PositionAlphabet(two) - 23

    if one == chr(choiceValue + 96).upper():
        return 3 + choiceValue

    winning = {"A": "Y", "B": "Z", "C": "X"}
    if (one, two) in winning.items():
        return 6 + choiceValue

    return 0 + choiceValue


def RockPaperScissorsTwo(one, outcome):
    outcome = (PositionAlphabet(outcome) - 24) * 3
    winning = {"A": "Y", "B": "Z", "C": "X"}
    losing = {"A": "Z", "B": "X", "C": "Y"}

    match outcome:
        case 3:
            return PositionAlphabet(one) + outcome

        case 0:
            two = losing[one]

        case 6:
            two = winning[one]

    return PositionAlphabet(two) - 23 + outcome


with open("2022/day02.input", "r") as f:
    lines = f.read().splitlines()

print(
    sum([RockPaperScissors(p1, p2) for x in lines for (p1, p2) in [x.split(" ")]]),
    sum([RockPaperScissorsTwo(p1, p2) for x in lines for (p1, p2) in [x.split(" ")]]),
)
