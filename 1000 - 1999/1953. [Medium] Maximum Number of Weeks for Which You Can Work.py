# https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/

class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        maxElem = max(milestones)
        aSum = sum(milestones)
        
        return aSum - max(0, 2*maxElem - aSum - 1)
                    
            
                    
            
