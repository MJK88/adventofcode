import numpy as np

# data collection
with open("2021/data04.in", "r") as f:
    lines = f.read().splitlines()

numbers = [int(x) for x in lines[0].split(",")]

lines = lines[1:]
list_of_matrices = []
for i in range(0, len(lines), 6):
    alist = [list(map(int, x.split())) for x in lines[i + 1 : i + 6]]
    list_of_matrices.append(np.array(alist, dtype=float))

bingo_cards = np.asarray(list_of_matrices)

# functions


def check_bingo(matrix):
    for i in range(matrix.shape[0]):
        if np.all(np.isnan(matrix[i])):
            return np.nansum(matrix, dtype=int)
    matrix = matrix.T
    for i in range(matrix.shape[0]):
        if np.all(np.isnan(matrix[i])):
            return np.nansum(matrix, dtype=int)


# part 1
for x in numbers:
    # replace bingo numbers with NaN
    bingo_cards[bingo_cards == x] = np.NAN
    # check for bingo
    for y in bingo_cards:
        if sum_unmarked := check_bingo(y):
            print(y)
            break
    # bingo!
    if sum_unmarked:
        print(
            f"first bingo! last number: {x}, sum: {sum_unmarked}, score: {x*sum_unmarked}"
        )
        break
    # no bingo (yet)
    else:
        pass

# part 2
index_of_bingo = dict()
for x in numbers:
    # replace bingo numbers with NaN
    bingo_cards[bingo_cards == x] = np.NAN
    # check for bingo
    for i, y in enumerate(bingo_cards):
        if sum_unmarked := check_bingo(y):
            if i not in index_of_bingo:
                index_of_bingo[i] = sum_unmarked * x

print(f"last bingo score: {list(index_of_bingo.values())[-1]}")
