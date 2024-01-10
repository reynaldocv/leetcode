# https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:    
       def helper(stack):
            seen = {(x, y) for (x, y) in stack}
            
            while stack: 
                (x, y) = stack.pop()
                
                for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    p, q = x + r, y + s
                    
                    if 0 <= p < m and 0 <= q < n: 
                        if heights[p][q] >= heights[x][y] and (p, q) not in seen: 
                            stack.append((p, q))
                            
                            seen.add((p, q))
                            
            return seen
        
        m, n = len(heights), len(heights[0])
        
        pacific = set([])
        atlantic = set([])
        
        for i in range(m):
            pacific.add((i, 0))
            atlantic.add((i, n - 1))
            
        for j in range(n):
            pacific.add((0, j))
            atlantic.add((m - 1, j))
            
        seen1 = helper([elem for elem in pacific])
        seen2 = helper([elem for elem in atlantic])
        
        ans = []
        
        for i in range(m):
            for j in range(n):
                if (i, j) in seen1 and (i, j) in seen2: 
                    ans.append((i, j))
                    
        return ans 
