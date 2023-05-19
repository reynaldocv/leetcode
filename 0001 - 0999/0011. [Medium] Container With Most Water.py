# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        
        start = 0 
        end = n - 1
        
        ans = 0 
        
        while end - start > 0: 
            ans = max(ans, min(height[start], height[end])*(end - start))
            
            if height[start] <= height[end]:
                start += 1 
        
            else: 
                end -= 1 
                
        return ans 
