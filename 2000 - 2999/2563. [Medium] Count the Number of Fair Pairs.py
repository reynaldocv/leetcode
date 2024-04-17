# https://leetcode.com/problems/count-the-number-of-fair-pairs/

class Solution:
    def coloredCells(self, n: int) -> int:
        return 2*n - 1 + 2*(n - 1)**2
        
