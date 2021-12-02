# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        ans = 0
        while right - left > 0:
            ans = max(ans, min(height[left], height[right])*(right - left))
            if height[left] < height[right]:
                left += 1
            else: 
                right -= 1
        
        return ans
