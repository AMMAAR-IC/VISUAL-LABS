import numpy as np

print(f"The version of numpy is{np.__version__}")
num = [1,2,3,4,5,6,7,8,9,0]
arr = np.array(num)

print(type(arr))
print(arr.shape)
print(arr.dtype)
print(arr.size)
print(arr.ndim)
print(arr.nbytes)

print(arr[0])
print(arr[1])
print(arr[-3])

print(arr[::])
