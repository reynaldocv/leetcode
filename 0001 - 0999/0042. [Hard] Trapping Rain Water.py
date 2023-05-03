# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        def helper(array):
            ans = [num for num in array]
            
            for i in range(1, n):
                ans[i] = max(ans[i], ans[i - 1])
                
            return ans 
        
        n = len(height)
        
        left = helper(height)
        right = helper(height[:: -1])[:: -1]
        
        ans = 0
        
        for i in range(n):
            ans += min(left[i], right[i]) - height[i]
            
        return ans 
       

        
