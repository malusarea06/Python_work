import array
import numpy as np
arr = array.array('b',[1,2,3])

for i in range(0,3):
    print(arr[i],end=" ")

print(arr.typecode)

print(np.dtype(np.int16))


