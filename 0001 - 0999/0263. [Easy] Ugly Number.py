# https://leetcode.com/problems/ugly-number/

class Solution:
    def isUgly(self, n: int) -> bool:
        numbers = [2, 3, 5]
        idx = 0
        while n > 1 and idx <= 2:
            while n % numbers[idx] == 0:
                n = n// numbers[idx]
            idx += 1
        
        return n == 1
        
        
        
    
