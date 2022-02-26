# https://leetcode.com/problems/count-servers-that-communicate/

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        counterR = defaultdict(lambda: 0)
        counterC = defaultdict(lambda: 0)
        ans = 0 
        positions = []
        
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: 
                    positions.append((i, j))
                    ans += 1 
                    counterR[i] += 1 
                    counterC[j] += 1 
        
        for (i, j) in positions: 
            if counterR[i] == 1 and counterC[j] == 1: 
                ans -= 1 
        
        return ans 
