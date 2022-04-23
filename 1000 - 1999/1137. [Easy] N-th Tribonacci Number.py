# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2: return n
        if n == 2: return 1
        fib3 = [1 for i in range(n + 1)]
        fib3[0] = 0
        for i in range(3, n + 1):
            fib3[i] = fib3[i - 1] + fib3[i - 2] + fib3[i - 3]
        
        return fib3[n]
    
class Solution2:
    def tribonacci(self, n: int) -> int:
        @cache
        def helper(i):
            if i <= 1: 
                return i 
            elif i == 2: 
                return 1 
            else: 
                return helper(i - 1) + helper(i - 2) + helper(i - 3)
            
        return helper(n)
        
        
