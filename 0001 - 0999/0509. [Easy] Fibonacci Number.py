# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, N: int) -> int:
        a = 0
        b = 1
        for i in range(0, N):
            a, b = b, a + b
        return a
        

