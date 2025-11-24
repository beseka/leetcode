class Solution(object):
    def maxArea(self, height):
        mx = 0 
        left = 0
        right = len(height)-1
        while left < right:
            area = min(height[left],height[right]) * (right-left)
            if area > mx :
                mx = area
            
            if height[left] < height[right]:
                left += 1  
            else:
                right -= 1

        return mx