# https://leetcode.com/problems/valid-perfect-square/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = -1 
        end = num 
        
        while end - start > 1: 
            mid = (end + start)//2
            
            if mid**2 < num: 
                start = mid 
            else: 
                end = mid 
            
        return end**2 == num
        
        
