# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, N: int) -> int:
        a = 0
        b = 1
        for i in range(0, N):
            a, b = b, a + b
        return a
        
class Solution2:
    def fib(self, n: int) -> int:
        @cache
        def helper(i):
            if i <= 1: 
                return i 
            else: 
                return helper(i - 1) + helper(i - 2)
            
        return helper(n)

