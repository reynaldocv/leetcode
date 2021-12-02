# https://leetcode.com/problems/valid-perfect-square/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 0 
        end = num + 1
        while end - start > 1: 
            m = (end + start)//2
            if m*m == num: 
                return True
            if m*m > num: 
                end = m
            else:
                start = m 
        return False 
        
