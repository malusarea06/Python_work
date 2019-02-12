import numpy as np

a = np.array([[1,2,3,4,5,6],
              [11,22,33,44,55,66],
              [21,22,23,24,25,26],
              [31,32,33,34,35,36],
              [41,42,43,44,45,46]])
# 2-D array
print(a)

#basic slicing

#print("\n a[0, 3:5]  = ", a[0, 3:5])

#print("\n a[4:, 4:]  = ", a[4:, 4:])

#print("\n a[:, 2]  = ", a[:, 2])

#print("\n a[2:;2, ::2]  = ", a[2::2,::2])

#print(a[...,:2])


n = np.array([10,40,80,50,25])

print(n)
print(n[n%40==0]**2)

# A 3 dimensional array.
b = np.array([[[1, 2, 3],[4, 5, 6]],
              [[7, 8, 9],[10, 11, 12]]])

print(b)


c = np.array([[5, 5],[4, 5],[16, 4]])
sumr = c.sum(-1)
print(sumr)

# Python program showing advanced indexing

a = np.array([[1, 2], [3, 4], [5, 6]])
print(a[[0, 1 , 2], [0,  1, 0]])



