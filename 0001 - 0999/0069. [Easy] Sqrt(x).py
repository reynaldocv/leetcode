# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x + 1
        
        while end - start > 1: 
            mid = (end + start)//2
            
            if mid**2 <= x: 
                start = mid
            else: 
                end = mid
                
        return start
            
        
