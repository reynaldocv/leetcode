# https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def helper(value):
            ans = 0 
            
            for quantity in quantities: 
                ans += ceil(quantity/value)
                
            return ans 
        
        start = 0 
        end = max(quantities)
        
        while end - start > 1: 
            mid = (end + start)//2 
            
            if helper(mid) > n: 
                start = mid 
                
            else: 
                end = mid
                
        return end 
            
            
        
