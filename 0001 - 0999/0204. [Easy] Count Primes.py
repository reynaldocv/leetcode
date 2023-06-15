# https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        dp = [1 for i in range(n)]
        
        ans = 0 
        
        for i in range(2, n):
            if dp[i] == 1: 
                ans += 1 
            
                for j in range(2*i, n, i):
                    dp[j] = 0 
                    
        return ans 
        
