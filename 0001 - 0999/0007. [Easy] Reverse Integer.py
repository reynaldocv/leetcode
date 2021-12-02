# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        aux = 1
        if x < 0:             
            aux = -1
        strx = str(x*aux)
        ans = aux*int(strx[::-1])
        if (-2**31 - 1 < ans < 2**31 - 1):
            return ans
        else:
            return 0
        
