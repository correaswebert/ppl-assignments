import pprint
import numpy as np
import scipy.linalg

A = np.array([
    [7, 3, -1, 2],
    [3, 8, 1, -4],
    [-1, 1, 4, -1],
    [2, -4, -1, 6]])
_, L, U = scipy.linalg.lu(A)

print("A:")
pprint.pprint(A)

print("L:")
pprint.pprint(L)

print("U:")
pprint.pprint(U)
