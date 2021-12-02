# https://leetcode.com/problems/prime-arrangements/

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def factorial(n):
            if n <= 1:
                return 1
            else:
                return n*factorial(n - 1)
            
        arr = [1 for i in range(n + 1)]
        primes = 0
        for i in range(2, n + 1):
            if arr[i] == 1:
                primes += 1
                for j in range(2*i, n + 1, i):
                    arr[j] += 1
        
        return (factorial(primes)*factorial(n - primes)) % (10**9 + 7)
        
