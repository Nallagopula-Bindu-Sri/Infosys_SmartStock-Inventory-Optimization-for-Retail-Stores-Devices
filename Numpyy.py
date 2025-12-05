import numpy as np
# 1. Create Arrays
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)
# 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", arr2)
# 2. Basic Properties
print("\nShape:", arr2.shape)
print("Dimensions:", arr2.ndim)
print("Size:", arr2.size)
print("Datatype:", arr2.dtype)
# 3. Indexing & Slicing
print("\narr[0]:", arr[0])
print("arr[1:4]:", arr[1:4])
print("arr2[1, 2]:", arr2[1, 2])   
print("arr2[:, 1]:", arr2[:, 1])  
# 4. Reshape
reshaped = arr2.reshape(3, 2)
print("\nReshaped (3x2):\n", reshaped)
# 5. Arithmetic Operations
print("\narr + 5:", arr + 5)
print("arr * 2:", arr * 2)
print("arr2 + arr2:\n", arr2 + arr2)
# 6. Concatenation
concat = np.concatenate([arr, np.array([60, 70])])
print("\nConcatenated Array:", concat)
# 7. Statistical Methods
print("\nMean:", arr.mean())
print("Max:", arr.max())
print("Min:", arr.min())
print("Sum:", arr.sum())
print("Standard Deviation:", arr.std())
