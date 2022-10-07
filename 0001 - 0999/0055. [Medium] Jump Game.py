# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = 0 
        
        for (i, num) in enumerate(nums):
            if i <= last: 
                last = max(last, i + num)
                
            else: 
                return False 
            
        return True 
            
                
        
