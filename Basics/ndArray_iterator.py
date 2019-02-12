import numpy as nump

a = nump.array([[1,2,3],[4,5,6],[7,8,9]])

for i in nump.nditer(a):
    print(i)