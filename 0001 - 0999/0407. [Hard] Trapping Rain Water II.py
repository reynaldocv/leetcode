# https://leetcode.com/problems/trapping-rain-water-ii/

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap: 
            return 0 
        
        n, m = len(heightMap), len(heightMap[0])
        heap, seen = [], {}
        
        for i in range(n):
            for j in range(m):
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    seen[(i, j)] = True
                    heappush(heap, (heightMap[i][j], i, j))
                 
        ans = 0
        
        while heap: 
            (cur, i, j) = heappop(heap)
            for (x, y) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < n and 0 <= y < m: 
                    if (x, y) not in seen: 
                        seen[(x, y)] = True
                        aux = heightMap[x][y]
                        if aux < cur: 
                            ans += cur - aux
                            heappush(heap, (cur, x, y))                        
                        else: 
                            heappush(heap, (aux, x, y))
                        
        return ans
