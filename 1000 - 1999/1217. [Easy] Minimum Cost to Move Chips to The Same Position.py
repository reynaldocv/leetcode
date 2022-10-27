# https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        ans = [0, 0]
        
        for x in position: 
            ans[x % 2] += 1 
            
        return min(ans)
        
