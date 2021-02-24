## Container With Most Water 
Two pointer O(N), O(1)
```python 
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
```