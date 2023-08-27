# https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/

class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        lower = target//2 
        
        if lower >= n: 
            lower = n
        
        upper = 0 
        
        if n - lower > 0: 
            upper = n - lower
        
        return lower*(lower + 1)//2 + target*upper + (upper)*(upper - 1)//2
        
