# https://leetcode.com/problems/super-pow/

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD, MOD2 = 190*6, 1337
        i, n = 1, len(b)
        exp = b[0]
        while i < n: 
            exp %= MOD
            exp = exp*10 + b[i]
            i += 1
        
        exp %= MOD
        
        return pow(a, exp, MOD2)
            
        
      
        
        
