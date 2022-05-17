# https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/

class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        start = bottom 
        
        special.sort() 
        
        ans = 0 
        
        for floor in special: 
            ans = max(ans, floor - start)
            start = floor + 1 
            
        ans = max(ans, top - start + 1)
        
        return ans 
