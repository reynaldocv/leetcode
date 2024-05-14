# https://leetcode.com/problems/reach-a-number/

class Solution:
    def reachNumber(self, target: int) -> int:
        def helper(value):
            return value*(value + 1)//2
        
        target = abs(target)
        
        start = 0 
        end = 10**9 
        
        while end - start > 1: 
            mid = (end + start)//2
            
            if helper(mid) < target: 
                start = mid 
                
            else: 
                end = mid 
                
        diff = helper(end) - target
        
        if diff % 2 == 0: 
            return end
        
        else: 
            return end + 1 + (end % 2)
        
        
