# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax, rightMax = [h for h in height],  [h for h in height]
        
        for i in range(1, n):
            leftMax[i] = max(leftMax[i], leftMax[i - 1])
        
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i], rightMax[i + 1])

        ans = 0 
        for i in range(1, n - 1):
            ans += min(leftMax[i], rightMax[i]) - height[i]
        
        return ans
  

        
