# https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = -inf
        
        minus = None 
        
        prev = 1 
        
        for num in nums: 
            prev*= num 
            
            if prev < 0: 
                if minus: 
                    ans = max(ans, prev//minus)
                    
                else: 
                    ans = max(ans, prev)
                    
                    minus = prev 
                    
            elif prev == 0: 
                ans = max(ans, 0)
                
                prev = 1 
                minus = None 
                
            else: 
                ans = max(ans, prev)
                
        return ans 
        
        
