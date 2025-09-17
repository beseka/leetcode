import numpy as np
class Solution(object):
    def majorityElement(self, nums):
        unique, frequency = np.unique(nums, 
                              return_counts = True)

        for i in frequency:
            if i > len(nums)/2:
                a = np.where(frequency ==i)[0][0]
                return unique[a]