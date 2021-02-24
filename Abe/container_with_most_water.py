"""
Container with most water

1. Clarify problem
2. edge cases
3. High level 
4. Solutions

input:  height = [1,8,6,2,5,4,8,3,7]
output: 48

"""

class Solution(object):
    def maxArea(self, height):
        max_area = 0
        left = 0
        right = len(height) -1
        
        while left < right:
            current_min = min(height[left], height[right])
            current_area = current_min * (right - left)
            max_area = max(current_area, max_area)
            
            # Choose biggest pointer
            if height[left] <= height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
                
        return max_area


# Test cases 
assert Solution().maxArea([1,8,6,2,5,4,8,3,7]) == 49, "Not correct answer"