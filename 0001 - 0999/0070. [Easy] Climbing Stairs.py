# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1: return 1
        f = [0]*(n)
        f[0] = 1
        f[1] = 2
        for i in range(2, n):
            f[i] = f[i - 1] + f[i - 2]
        
        return f[n - 1]
        
class Solution2:
    def climbStairs(self, n: int) -> int:
        @cache
        def helper(i):
            if i <= 2: 
                return i 
            else: 
                return helper(i - 1) + helper(i - 2)
            
        return helper(n)
        
        
