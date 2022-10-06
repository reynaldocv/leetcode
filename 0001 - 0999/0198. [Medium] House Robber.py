# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        ans = 0 
        
        for i in range(n):
            val3 = nums[i - 3] if i - 3 >= 0 else 0
            val2 = nums[i - 2] if i - 2 >= 0 else 0 
            
            nums[i] += max(val3, val2)
            
            ans = max(ans, nums[i])
            
        return ans 
            
        
