# https://leetcode.com/problems/preimage-size-of-factorial-zeroes-function/

class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def helper(value, div):
            ans = 0 
            
            while value > 0: 
                ans += (value//div)
                
                value //= div
                
            return ans 
        
        def collaborate(qnt):
            start = -1
            end = 2**32
            
            while end - start > 1: 
                mid = (end + start)//2
                
                if helper(mid, 5) < qnt:
                    start = mid 
                    
                else: 
                    end = mid 
                    
            return end 
        
        right = collaborate(k + 1)
        left = collaborate(k)
        
        return right - left
