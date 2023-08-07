# https://leetcode.com/problems/find-the-safest-path-in-a-grid/

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        distances = [[0 for _ in range(m)] for _ in range(n)]
        
        stack = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1]
        seen = set(stack)
        
        steps = 0 
        
        while stack: 
            newStack = []
            
            for (x, y) in stack: 
                distances[x][y] = steps
                
                for (r, s) in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                    p, q = x + r, y + s
                    
                    if 0 <= p < m and 0 <= q < n: 
                        if (p, q) not in seen: 
                            seen.add((p, q))
                            
                            newStack.append((p, q))
            
            stack = newStack 
            steps += 1 
             
        heap = [(-distances[0][0], 0, 0)]
        seen = {(0, 0)}
        
        while heap: 
            (ans, x, y) = heappop(heap)
            
            if x == m - 1 and y == n - 1: 
                return -ans
            
            for (r, s) in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                p, q = x + r, y + s
                    
                if 0 <= p < m and 0 <= q < n: 
                    if (p, q) not in seen: 
                        seen.add((p, q))

                        heappush(heap, (max(ans, -distances[p][q]), p, q))

