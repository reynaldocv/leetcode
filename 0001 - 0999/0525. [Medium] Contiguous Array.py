# https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = {0: -1}
        
        ans = 0 
        
        cnt = 0 
        
        for (i, num) in enumerate(nums): 
            if num == 1: 
                cnt += 1 
                
            else:
                cnt -= 1 
                
            if cnt in seen: 
                ans = max(ans, i - seen[cnt])
            
            else: 
                seen[cnt] = i 
            
        return ans 
        
            
            
        
        
