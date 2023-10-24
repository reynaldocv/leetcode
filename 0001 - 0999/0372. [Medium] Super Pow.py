# https://leetcode.com/problems/super-pow/

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        
        ans = 1
        
        for exp in b: 
            ans = pow(ans, 10, MOD) * pow(a, exp, MOD)
        
        return ans % 1337

        
        
        
