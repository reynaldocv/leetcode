# https://leetcode.com/problems/count-the-hidden-sequences/

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int: 
        n = len(differences)
        maxDiff, minDiff = 0, 0
        
        prev = 0
        
        for diff in differences: 
            prev += diff
            maxDiff = max(maxDiff, prev)
            minDiff = min(minDiff, prev)
            
        maxStart = upper - maxDiff
        minStart = lower - minDiff 
        
        return max(0, maxStart - minStart + 1)
    
