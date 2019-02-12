import numpy as np

arr = np.array([[1,2,3],[4,2,5],[6,7,8]])

print("Array is of type: ",type(arr))
print("Dimension : ",arr.ndim)
print("Shape of array : ",arr.shape)
print("Array size : ",arr.size)
print("Array elements type : ",arr.dtype)


tp = ('aniket','16','M')
tuparr = np.array(tp)

print(tuparr.dtype)
zer = np.zeros((3,3))

arr1 = np.full((2,2),5,dtype='int32')
print(arr1)



