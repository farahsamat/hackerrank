import numpy as np

arr = np.random.randint(-9, 9, (6, 6))


def hourglassSum(arr):
    hourglasslist = []
    for i in range(4):
        for j in range(4):
            sumhourglass = np.sum(arr[i][j:j + 3]) + arr[i + 1][j + 1] + np.sum(arr[i + 2][j:j + 3])
            hourglasslist.append(sumhourglass)
    return max(hourglasslist)


print(arr)
print(hourglassSum(arr))
