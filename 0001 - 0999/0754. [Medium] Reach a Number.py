# https://leetcode.com/problems/reach-a-number/

class Solution:
    def reachNumber(self, target: int) -> int:
        if target == 0: 
            return 0 
        if target < 0: 
            target *= -1
            
        steps = int((-1 + (1 + 8*target)**.5)/2)
        
        while steps*(steps + 1)//2 < target:
            steps += 1
        
        spaces = target - steps*(steps + 1)//2
        if spaces % 2 == 1:
            if steps % 2 == 0: 
                steps += 1
            else: 
                steps += 2
        
        return steps
        
        https://leetcode.com/problems/reach-a-number/
