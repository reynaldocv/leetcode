# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = 0 
        
        negative = None         
        positive = -1
        
        prev = 1 
        
        for (i, num) in enumerate(nums): 
            if num < 0: 
                prev *= -1
                
            elif num == 0: 
                prev = 0 
            
            if prev > 0: 
                ans = max(ans, i - positive)
                
            elif prev < 0: 
                if negative != None: 
                    ans = max(ans, i - negative)
                    
                else: 
                    negative = i 
                    
            else: 
                prev = 1
                
                positive = i                 
                negative = None
                    
        return ans 
            
        
        
