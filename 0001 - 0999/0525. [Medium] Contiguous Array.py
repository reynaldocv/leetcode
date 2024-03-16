# https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        last = {0: -1}
        
        ans = prev = 0 
        
        for (i, num) in enumerate(nums): 
            if num == 0: 
                prev -= 1 
                
            else: 
                prev += 1 
                
            if prev in last: 
                ans = max(ans, i - last[prev])
                
            else: 
                last[prev] = i 
                
        return ans 
        
            
            
        
        
