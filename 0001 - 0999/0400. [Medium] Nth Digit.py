# https://leetcode.com/problems/nth-digit/

class Solution:
    def findNthDigit(self, n: int) -> int:
        start = 1        
      
        ratio = 1
        lvl = 1        
        
        while n > 9*ratio*lvl: 
            n -= 9*ratio*lvl
            
            ratio *= 10 
            lvl += 1 
            
            start *= 10
            
        start += (n - 1)//lvl 
        
        position = n % lvl
        
        return int(str(start)[position - 1])
        
        
