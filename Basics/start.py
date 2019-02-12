import numpy as np

#creating array and characterstics of array

a = np.array([[[1,4,2,3],[3,4,3,3],[5,6,4,5]],
             [[1,4,2,3],[3,4,3,3],[5,6,4,5]],
             [[1,2,3,4],[4,5,5,6],[35,65,6,55]]])

print(a.dtype)
print(a.size)
print('shape of array :',a.shape)
print(a[1][0][1])

#Slicing an array

arr = np.array([[-1, 2, 0, 4, 5],
                [4, -0.5, 6, 0, -2],
                [2.6, 0, 7, 8, -3],
                [3, -7, 4, 2.0, -6]])

temp = arr[::2,::3]
print('------------------')
cond = arr > 2
tmp = arr[cond]

print(tmp)


#operations on single array


arr = np.array([1,2,3,4])
arr*=3
print('Array Dimension : ',arr.ndim)


#transpose array

a = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(a)
print('---------------')
print(a.shape)
print(arr.max(axis=1))


#Unary Operations
print('===================')
print(a.ndim)
print(a.min(axis=1))






