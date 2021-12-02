# https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/

class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        ans = 0
        minX = min(startPos[0], homePos[0])
        maxX = max(startPos[0], homePos[0])
        
        minY = min(startPos[1], homePos[1])
        maxY = max(startPos[1], homePos[1])
        
        for i in range(minX, maxX + 1):
            ans += rowCosts[i]
        
        for i in range(minY, maxY + 1):
            ans += colCosts[i]
            
        return ans - rowCosts[startPos[0]] - colCosts[startPos[1]]
        
        
