with open("2024/day05.input", "r") as f:
    lines = f.read().split("\n\n")

example = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""".split(
    "\n\n"
)

pageOrdening = [x.split("|") for x in lines[0].split("\n")]
pagesToProduce = [x.split(",") for x in lines[1].split("\n")]


def CorrectOrder(update, pageOrdening):

    for pageNumber in update:
        allNumbersAfter = [
            x[1] for x in pageOrdening if x[0] == pageNumber and x[1] in update
        ]
        if any(
            update.index(after) < update.index(pageNumber) for after in allNumbersAfter
        ):
            return False

        allNumbersBefore = [
            x[0] for x in pageOrdening if x[1] == pageNumber and x[0] in update
        ]
        if any(
            update.index(before) > update.index(pageNumber)
            for before in allNumbersBefore
        ):
            return False

    return True


def GetNewUpdate(update, pageOrdening):
    newUpdate = ["."] * len(update)
    for pageNumber in update:
        allNumbersBefore = [
            x[0] for x in pageOrdening if x[1] == pageNumber and x[0] in update
        ]
        newUpdate[len(allNumbersBefore)] = pageNumber

    return newUpdate


sum = 0
sum2 = 0
for update in pagesToProduce:
    if CorrectOrder(update, pageOrdening):
        sum += int(update[len(update) // 2])
    else:
        newUpdate = GetNewUpdate(update, pageOrdening)
        sum2 += int(newUpdate[len(newUpdate) // 2])

print(sum)
print(sum2)
