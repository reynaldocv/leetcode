# https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(num, n):
            if n == 0: 
                return 1 
            
            elif n == 1: 
                return num
            
            elif n % 2 == 0: 
                return helper(num**2, n//2)
            
            else: 
                return num*helper(num, n - 1)
            
        if n < 0: 
            n *= -1
            x = 1/x
            
        return helper(x, n)
        
