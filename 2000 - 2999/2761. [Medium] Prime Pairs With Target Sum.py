# https://leetcode.com/problems/prime-pairs-with-target-sum/

class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        primes = [0, 0 ] + [1 for _ in range(n)]
        
        for i in range(2, n):
            if primes[i] == 1: 
                for j in range(2*i, n, i):
                    primes[j] = 0 
                    
        ans = []
        
        for i in range(2, n//2 + 1):
            if primes[i] == 1 and primes[n - i] == 1: 
                ans.append((i, n - i))
                
        return ans 
