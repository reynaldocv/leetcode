# https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        maxC = [max(i) for i in grid]
        maxR = []
        for R in range(len(grid[0])):
            aux = []
            for C in range(len(grid)):
                 aux.append(grid[C][R])
            maxR.append(max(aux))
        ans = 0
        for C in range(len(grid)):
            for R in range(len(grid[0])):
                 ans += min(maxC[C], maxR[R]) - grid[C][R]
        return ans        
