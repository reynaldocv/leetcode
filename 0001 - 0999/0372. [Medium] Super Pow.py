# https://leetcode.com/problems/super-pow/

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        
        ans = 1
        
        for (i, num) in enumerate(b[:: -1]):
            ans *= pow(a, num*10**i, MOD)
            
        return ans % MOD 
        
        
        
