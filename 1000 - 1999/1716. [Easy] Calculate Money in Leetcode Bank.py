# https://leetcode.com/problems/calculate-money-in-leetcode-bank/

class Solution:
    def totalMoney(self, n: int) -> int:
        start = -1
        end = n 
        
        quotient = n//7
        remain = n % 7 
        
        ans = quotient*(quotient - 1)*7//2 + (quotient)*28
        
        for num in range(1, remain + 1):
            ans += quotient + num
            
        return ans 
        
