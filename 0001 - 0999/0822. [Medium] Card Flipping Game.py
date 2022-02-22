# https://leetcode.com/problems/card-flipping-game/

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        seen = {}
        n = len(fronts)
        
        for i in range(n):
            if fronts[i] == backs[i]:
                seen[fronts[i]] = True 
                
        ans = inf
        
        for val in fronts + backs: 
            if val not in seen: 
                ans = min(ans, val)
                
        return 0 if ans == inf else ans
