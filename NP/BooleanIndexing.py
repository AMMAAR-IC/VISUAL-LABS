import numpy as np

arr = np.array([1, 2, 3, 4, 5])
def alt(arr):
    mask = np.array([True, False, True, False, True])
    return arr[mask]

print(alt(arr))
