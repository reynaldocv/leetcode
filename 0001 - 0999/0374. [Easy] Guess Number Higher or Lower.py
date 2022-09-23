# https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 0 
        end = n 
        
        while end - start > 1: 
            mid = (end + start)//2
            
            if guess(mid) == 1: 
                start = mid 
            else: 
                end = mid
                
        return end 
    
