import numpy as np

nums = np.array([1,100,1])
t = len(nums)
target = 16

for i in range (1, len(nums)):
    if i >= 0 and i < t :
        list = [(nums[i], nums[i+1], nums[i+2], nums[i+3])]
        sum_list = sum(list)
        sum_list = target
    print(list)
print(sum_list)   

             