# https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7 
        
        middle = n//2 
        
        first = pow(5, middle, MOD)
        second = pow(4, middle, MOD)
        
        ans = (first*second) % MOD
            
        if n % 2 == 1: 
            ans = (5*ans) % MOD 
            
        return ans
