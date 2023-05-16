# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        @cache
        def helper(number):
            ans = 0 
            
            while number: 
                ans += (number % 10)**2
                
                number //= 10 
                
            return ans 
        
        seen = {1}
        
        while n not in seen: 
            seen.add(n)
            
            n = helper(n)
            
        return n == 1
            
        
        
