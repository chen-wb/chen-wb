import numpy as np


# 初始化一个10*10的数组
mtx = np.array([
    [np.NaN, np.NaN, np.NaN, 3, 4, 5, 6, 7, 8, 9],
    [np.NaN, np.NaN, 3, 4, 5, 6, 7, 8, 9, 0],
    [2, 3, 4, 5, 6, 7, 8, 9, 0, 1],
    [3, 4, 5, 6, 7, 8, 9, 0, 1, 2],
    [4, 5, 6, 7, 8, 9, 0, 1, 2, 3],
    [5, 6, 7, 8, 9, 0, 1, 2, 3, 4],
    [6, 7, 8, 9, 0, 1, 2, 3, 4, 5],
    [7, 8, 9, 0, 1, 2, 3, 4, 5, 6],
    [8, 9, 0, 1, 2, 3, 4, 5, 6, 7],
    [9, 0, 1, 2, 3, 4, 5, 6, 7, 8],
])


def nan_value_count(array: np.array):
    '''
    返回数组中的值为NaN的数量
    '''
    x, y = array.shape

    count = 0
    for i in range(x):
        for j in range(y):
            if np.isnan(array[i, j]):
                count += 1

    return count

# 取mtx数组的行和列数
x, y = mtx.shape
xlength = 3; ylength = 3

for i in range(x // xlength):
    for j in range(y // ylength):
        mtx0 = mtx[i * xlength : (i + 1) * xlength, j * ylength : (j + 1) * ylength]
        # print(nan_value_count(mtx0))
        if nan_value_count(mtx0) < xlength * ylength * 0.5:
            print(np.nanmean(mtx0))
        else:
            print(np.NaN)


