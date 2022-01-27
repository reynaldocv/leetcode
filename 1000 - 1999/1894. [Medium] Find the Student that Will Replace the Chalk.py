# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        aSum = sum(chalk)
        k = k % aSum 
        
        for (i, val) in enumerate(chalk):
            if k < val: 
                return i
            else: 
                k -= val
                
        
        
