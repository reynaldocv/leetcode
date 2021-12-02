# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = 0 
        n = len(nums)
        for i in range(n):            
            if i <= end:
                end = max(i + nums[i], end)        
            else: 
                return False
        return True if end >= n - 1 else False
            
                
        
