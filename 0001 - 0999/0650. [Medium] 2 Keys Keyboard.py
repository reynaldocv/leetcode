# https://leetcode.com/problems/2-keys-keyboard/

class Solution:
    def minSteps(self, n: int) -> int:
        ans = 0 
        
        div = 2 
        
        while n > 1: 
            while n % div == 0: 
                ans += div 
                
                n /= div 
                
            div += 1 
            
        return ans
        
            
