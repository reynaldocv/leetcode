# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        @cache
        def helper(x):
            ans = 0 
            
            while x:
                ans += (x % 10)**2
                
                x //= 10
                
            return ans 
                
        seen = {1}
        
        while n not in seen: 
            seen.add(n)
            
            n = helper(n)
            
        return n == 1
        
        
