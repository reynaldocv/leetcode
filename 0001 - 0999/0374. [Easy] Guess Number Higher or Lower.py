# https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1: return 1
        start = 0
        end = n + 1        
        while (end - start > 1):
            m = (start + end)//2
            r = guess(m)
            if r == 0: 
                return m
            elif r == -1:
                end = m
            else:
                start = m
        return end
