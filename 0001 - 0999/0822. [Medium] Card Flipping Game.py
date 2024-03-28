# https://leetcode.com/problems/card-flipping-game/

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        n = len(fronts)
        
        seen = set() 
                
        for i in range(n):
            if fronts[i] == backs[i]:
                seen.add(fronts[i])
                
        ans = inf 
        
        for i in range(n):
            if fronts[i] not in seen: 
                ans = min(ans, fronts[i])
            
            if backs[i] not in seen: 
                ans = min(ans, backs[i])
                
        return 0 if ans == inf else ans
