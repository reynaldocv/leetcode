# https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:        
        seen = {0: -1}
        counter = 0 
        ans = 0
        for (i, val) in enumerate(nums): 
            counter += 1 if val == 1 else -1
            if counter in seen: 
                ans = max(ans, i - seen[counter])
            else: 
                seen[counter] = i
                
        return ans
           
            
            
        
        
