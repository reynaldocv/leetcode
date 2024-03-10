# https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/

class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        minX = min(startPos[0], homePos[0])
        maxX = max(startPos[0], homePos[0])
        
        minY = min(startPos[1], homePos[1])
        maxY = max(startPos[1], homePos[1])
        
        ans = sum(colCosts[minY: maxY + 1]) + sum(rowCosts[minX: maxX + 1])
        
        ans -= colCosts[startPos[1]] + rowCosts[startPos[0]]
        
        return ans 
        
        
        
