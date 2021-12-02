# https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = int(c**.5)
        for i in range(n + 1):
            j = int((c - i**2)**.5)
            if i**2 + j**2 == c:              
                return True
        return False
        
