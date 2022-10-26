# https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prev = 0 
        
        seen = {prev: -1}
        
        for (i, num) in enumerate(nums): 
            prev = (prev + num) % k 
            
            if prev in seen: 
                if (i - seen[prev]) >= 2: 
                    return True 
                
            else: 
                seen[prev] = i 
                
        return False 
    
            
                
                
                
                
        
