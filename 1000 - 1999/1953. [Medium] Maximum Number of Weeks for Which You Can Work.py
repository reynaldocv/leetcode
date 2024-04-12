# https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/

class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        aSum = sum(milestones)
        maxStones = max(milestones)
        
        left = aSum - maxStones
        
        if left < maxStones: 
            return 2*left + 1
        
        else: 
            return aSum 
            
