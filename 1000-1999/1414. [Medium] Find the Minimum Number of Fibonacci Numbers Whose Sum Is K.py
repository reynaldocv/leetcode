# https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        @cache
        def helper(n):
            if n <= 1: 
                return 1
            else: 
                return helper(n - 1) + helper(n - 2)
            
        fibonacci = []    
        i = 1
        while helper(i) <= k:
            fibonacci.append(helper(i))
            i += 1
            
        ans = 0 
        while k > 0: 
            idx = bisect_left(fibonacci, k)
            if idx == len(fibonacci) or fibonacci[idx] > k:
                idx -= 1
            k -= fibonacci[idx]
            ans += 1    
            
        return ans
        
