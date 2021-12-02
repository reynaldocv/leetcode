# https://leetcode.com/problems/nth-digit/

class Solution:
    def findNthDigit(self, n: int) -> int:
        base, dig = 1, 1
        while n > 9*base*dig:
            n -= 9*base*dig          
            base *= 10
            dig += 1
        
        quo = n // dig
        res = n % dig      
        
        if res == 0:
            quo -= 1
            
        num = base + quo
        
        if res == 0: 
            return int(str(num)[-1])
        else: 
            return int(str(num)[res - 1])
