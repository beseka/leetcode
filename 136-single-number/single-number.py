class Solution(object):
    def singleNumber(self, nums):
        a = []
        for i in nums:
            if i not in a:
                a.append(i)
            else:
                a.remove(i)
        
        return int(a[0])

        