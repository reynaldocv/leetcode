# https://leetcode.com/problems/arranging-coins/ 

class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1: return 1
        m = int((2*n)**.5)        
        while m*(m + 1)//2 <= n:
            m += 1
        return m - 1
        
