import numpy as np


def IsThisTreeVisible(height, trees):
    return all(height > trees)


def ScenicScore(height, trees):
    num = 0
    for x in trees:
        if height <= x:
            num += 1
            break
        num += 1
    return num


with open("2022/day08.input", "r") as f:
    lines = f.read().splitlines()

trees = np.array([[int(y) for y in x] for x in lines])

visible = np.ones(trees.shape, dtype=int)
visible[1:-1, 1:-1] = 0

scenicScore = np.zeros(trees.shape, dtype=int)

for row in range(1, trees.shape[0] - 1):
    for col in range(1, trees.shape[1] - 1):
        # from top
        if IsThisTreeVisible(trees[row, col], trees[:row, col]):
            visible[row, col] += 1
        # from bottom
        if IsThisTreeVisible(trees[row, col], trees[row + 1 :, col]):
            visible[row, col] += 1
        # from left
        if IsThisTreeVisible(trees[row, col], trees[row, :col]):
            visible[row, col] += 1
        # from right
        if IsThisTreeVisible(trees[row, col], trees[row, col + 1 :]):
            visible[row, col] += 1

        scenicScore[row, col] = (
            ScenicScore(trees[row, col], np.flip(trees[:row, col]))
            * ScenicScore(trees[row, col], trees[row + 1 :, col])
            * ScenicScore(trees[row, col], np.flip(trees[row, :col]))
            * ScenicScore(trees[row, col], trees[row, col + 1 :])
        )

numberOfVisibleTrees = np.count_nonzero(visible)
highestScenicScore = np.max(scenicScore)
print(numberOfVisibleTrees)
print(highestScenicScore)
