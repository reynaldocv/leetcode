# https://leetcode.com/problems/domino-and-tromino-tiling/

class Solution:
    def numTilings(self, n: int) -> int:        
        @cache
        def p(n):
            if n == 2: 
                return 1
            
            return (p(n - 1) + f(n - 2)) % MOD
        
        @cache
        def f(n):
            if n <= 2: 
                return n 
            
            return (f(n - 1) + f(n - 2) + 2*p(n - 1)) % MOD
        
        MOD = 10**9 + 7
        
        return f(n)
