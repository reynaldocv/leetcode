# https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int:
        def helper(num):
            ans = 0 
            
            div = 2
            
            while num > 1: 
                while num % div == 0: 
                    num //= div
                    
                    ans += div
                    
                div += 1 
                
            return ans 
        
        seen = set()
        
        while n not in seen: 
            seen.add(n)
            
            n = helper(n)
            
        return n 
        
