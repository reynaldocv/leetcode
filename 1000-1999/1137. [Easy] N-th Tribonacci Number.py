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
        
        
