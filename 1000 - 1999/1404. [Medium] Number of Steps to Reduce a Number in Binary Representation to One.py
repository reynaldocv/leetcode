# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, 2)
        
        ans = 0 
        
        while num > 1: 
            if num % 2 == 0: 
                num //= 2
                
            else: 
                num += 1 
                
            ans += 1 
            
        return ans 
            
        
        
