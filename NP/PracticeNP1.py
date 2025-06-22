import numpy as np

# array
arr = np.array([1, 2, 3, 4, 5, 6])

# array indexing
print(arr[0])

# some exl array fns
print(np.arange(1, 20, 1))
print(np.linspace(1, 20, 100))
print(np.zeros(10))
print(np.ones(2))

# N-D arrays

# 1D
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# 2D
arr2 = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10]])
# 3D
arr3 = np.array([
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]],

    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
])

# Boolean filtering
arr4 = np.array([1, 2, 3, 4])
mask = np.array([True, False, True, False])
print(arr4[mask])
