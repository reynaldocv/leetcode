# https://leetcode.com/problems/add-minimum-number-of-rungs/

class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        n = len(rungs)
        
        ans = 0 
        
        last = 0 
        for i in range(n):
            if rungs[i] - last > dist: 
                distance = rungs[i] - last
                quo = distance//dist
                ans += quo - 1 if distance % dist == 0 else quo
                
            last = rungs[i]
                
        return ans
                
        
        
            
       
