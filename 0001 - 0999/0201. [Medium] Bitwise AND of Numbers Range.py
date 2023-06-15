# https://leetcode.com/problems/bitwise-and-of-numbers-range/ 

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0 
        
        while left != right: 
            left //= 2 
            right //= 2 
            
            count += 1 
            
        return left << count
            
        
