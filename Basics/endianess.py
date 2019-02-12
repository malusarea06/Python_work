import numpy as np

list = [1,2,3,4,5,6]
n = np.array(list)

print(n)

a = np.arange(10,1,-1)

print("New Array : ",a)

print(n[np.array([0,1,-1])])
print(n[-2:1:-1])