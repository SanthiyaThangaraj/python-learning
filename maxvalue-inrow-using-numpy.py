#Create a 4x4 array with random integers between 1 and 100. Find the maximum value in each row

import numpy as np
arr=np.random.randint(1,101,(4,4))
max_values=arr.max(axis=1)
print("4x4 array : ",arr)
print("maximum value in each row: ",max_values)
            
