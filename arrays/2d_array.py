import numpy as np

arr = np.random.randint(-9, 9, (6, 6))


def hourglassSum(arr):
    hourglasslist = []
    for i in range(4):
        for j in range(4):
            subhourglasslist = []
            subhourglasslist.extend([sum(list(arr[i][j:j + 3])), arr[i + 1][j + 1], sum(list(arr[i + 2][j:j + 3]))])
            hourglasslist.append(sum(subhourglasslist))
    return max(hourglasslist)


print(arr)
print(hourglassSum(arr))
