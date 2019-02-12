import numpy as nump

array = nump.arange(1,9).reshape([2,4])

print(array)
print('--------------------')
print('numpy with axis 0')
print('--------------------')
print(nump.sum(array,axis=0))
print('--------------------')
print('numpy with axis 1')
print('--------------------')
print(nump.sum(array,axis=1))



#concatination of array

np_array_1s = nump.array([[1,1,1],[1,1,1]])
np_array_9s = nump.array([[9,9,9],[9,9,9]])

a = nump.concatenate([np_array_1s, np_array_9s], axis = 1)

#print(a)



#numpy sum with axis 0 anmd 1

np_arr = nump.array([[1,2,3],[4,5,6]])
print(nump.sum(np_arr,axis=1))
