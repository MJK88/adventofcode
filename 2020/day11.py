import numpy as np

with open("data11.in", "r") as f:
    lines = f.read().splitlines()

M = np.array([list(x) for x in lines])
# surround with dots to prevent out-of-range problems
M = np.pad(M, pad_width=1, mode="constant", constant_values=".")


def adjacent_seats(x, y):
    # Create matrix of the nearest neighbors
    N = M[x - 1 : x + 2, y - 1 : y + 2]
    # return number of adjacents seats minus the center one
    return np.sum(N == "#") - 1


newM = M.copy()
while True:
    num_seats_before = np.sum(M == "#")
    for row in range(1, M.shape[0] - 1):
        for col in range(1, M.shape[1] - 1):
            if M[row, col] == "L" and adjacent_seats(row, col) == -1:
                newM[row, col] = "#"
            elif M[row, col] == "#" and adjacent_seats(row, col) >= 4:
                newM[row, col] = "L"
    M = newM.copy()
    if num_seats_before == np.sum(M == "#"):
        break

print(num_seats_before)

# part 2
def seats_in_view(x, y):
    n = 0

    return n


newM = M.copy()
while True:
    num_seats_before = np.sum(M == "#")
    for row in range(1, M.shape[0] - 1):
        for col in range(1, M.shape[1] - 1):
            if M[row, col] == "L" and seats_in_view(row, col) == -1:
                newM[row, col] = "#"
            elif M[row, col] == "#" and seats_in_view(row, col) >= 5:
                newM[row, col] = "L"
    M = newM.copy()
    if num_seats_before == np.sum(M == "#"):
        break

print(num_seats_before)
