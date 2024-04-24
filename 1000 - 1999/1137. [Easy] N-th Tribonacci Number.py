# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:
        @cache 
        def helper(n):
            if n <= 2: 
                return [0, 1, 1][n]
            
            else: 
                return helper(n - 1) + helper(n - 2) + helper(n - 3)
            
        return helper(n)
    
