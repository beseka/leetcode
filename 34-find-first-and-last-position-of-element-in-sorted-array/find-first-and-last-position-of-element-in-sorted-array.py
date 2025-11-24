class Solution(object):
    def searchRange(self, nums, target):
        ind = []
        if target not in nums:
            return [-1,-1]

        a = nums.index(target)
        ind.append(a)
        while nums[a] == target:
            if (a+1) < len(nums) and nums[a+1] == target:
                a = a+1
            else:
                ind.append(a)
                break


        return ind
        