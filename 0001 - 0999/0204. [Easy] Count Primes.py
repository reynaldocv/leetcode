# https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [1 for i in range(n)]
        
        ans = 0
        for i in range(2, n):
            if primes[i] == 1:
                ans += 1
                for j in range(2*i, n, i):                    
                    primes[j] += 1
           
        
        return ans
