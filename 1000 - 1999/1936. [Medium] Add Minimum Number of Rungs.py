# https://leetcode.com/problems/add-minimum-number-of-rungs/

class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        start = 0
            
        ans = 0 
        
        for num in rungs: 
            if start + dist < num: 
                ans += (num - start - 1)//dist
                
            start = num 
            
        return ans 
        
        
        
            
       
