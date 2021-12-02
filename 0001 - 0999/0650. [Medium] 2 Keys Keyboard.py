# https://leetcode.com/problems/2-keys-keyboard/

class Solution:
    def minSteps(self, n: int) -> int:
        exp = {}
        
        while n % 2 == 0: 
            exp[2] = exp.get(2, 0) + 1
            n = n//2
        
        b = 3
        while n > 1: 
            while n % b == 0: 
                exp[b] = exp.get(b, 0) + 1
                n = n // b
            b += 2
        
        ans = 0
        for key in exp: 
            ans  += key*exp[key]
        
        return ans
            
