# https://leetcode.com/problems/minimum-levels-to-gain-more-points/

class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        n = len(possible)
        
        Alice = 0 
        Bob = sum(possible) - (n - sum(possible))
        
        ans = (-inf, -1)
        
        for (ith, num) in enumerate(possible[: -1]):
            if num == 0: 
                Alice -= 1 
                Bob += 1 
                
            else: 
                Alice += 1 
                Bob -= 1 
                
            if Alice > Bob: 
                return ith + 1
            
        return -1 
