# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x
        while end - start > 1: 
            m = (start + end)//2
            if m*m == x:
                return m 
            if m*m >= x:
                end = m
            else:
                start = m
        if end*end == x:            
            return end
        return start
            
        
