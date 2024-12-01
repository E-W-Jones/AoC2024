import numpy as np
col1, col2 = np.loadtxt("input.txt", unpack=True, dtype=int)
col1.sort()
col2.sort()
# Task 1
print(np.sum(np.abs(col1 - col2)))
# Task 2
print(sum(x * np.count_nonzero(col2 == x) for x in col1))