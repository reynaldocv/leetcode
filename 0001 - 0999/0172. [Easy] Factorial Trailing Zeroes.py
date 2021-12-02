# https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        aux = 5
        ans = 0
        while n >= aux:
            ans += n//aux
            aux *= 5
        return ans
            
