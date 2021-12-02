# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        total = high - low + 1
        if low % 2 == 1:
            return total//2 + 1 if (total % 2 == 1) else total//2
        else: 
            return total//2
            
