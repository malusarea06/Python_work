import numpy as np

arr = np.array([[1,2,3,4],[4,3,4,2],[1,5,3,2],[9,4,6,7]])

print(arr[:2,:3])

Index_arr = arr[[1, 1, 0, 3],
                [3, 2, 1, 0]]
print ("\nElements at indices (1, 3), "
    "(1, 2), (0, 1), (3, 0):\n", Index_arr)
