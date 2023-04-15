# https://leetcode.com/problems/prime-in-diagonal/

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        maxElem = max(max(row) for row in nums)
        
        primes = set()
        
        dp = [1 for _ in range(maxElem + 1)]
        
        for i in range(2, maxElem + 1):
            if dp[i] == 1: 
                primes.add(i)
                
                for j in range(2*i, maxElem + 1, i):
                    dp[j] += 1 
        
        n = len(nums)
        
        ans = 0 
        
        for i in range(n):
            if nums[i][i] in primes: 
                ans = max(ans, nums[i][i])
                
            if nums[i][n - i - 1] in primes: 
                ans = max(ans, nums[i][n - i - 1])
                
        return ans 
        
        
        
