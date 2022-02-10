# https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7        
        m = n//2        
        ans = pow(20, m, MOD)
        
        if n % 2 != 0: 
            ans *= 5
            
        return ans % MOD
