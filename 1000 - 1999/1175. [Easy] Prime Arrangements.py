# https://leetcode.com/problems/prime-arrangements/

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        if n <= 2: 
            1 
        
        MOD = 10**9 + 7
        
        dp = [1 for _ in range(n + 1)]
        
        primes = 0 
        
        for i in range(2, n + 1):
            if dp[i] == 1: 
                primes += 1 
                
            for j in range(2*i, n + 1, i):
                dp[j] += 1 
                
        ans = 1 
        
        for i in range(2, primes + 1):
            ans = (ans*i) % MOD
            
        for i in range(2, n - primes + 1):
            ans = (ans*i) % MOD
            
        return ans 
        
