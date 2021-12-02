# https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:    
        if not heights: 
            return []
        
        n, m = len(heights), len(heights[0])
        
        arr1 = [[0 for _ in range(m)] for _ in range(n)]
        arr2 = [[0 for _ in range(m)] for _ in range(n)]
        
        seen = {}
        stack = []
        for i in range(n):
            arr1[i][0] = 1
            seen[(i, 0)] = True
            stack.append((i, 0))
        
        for j in range(m):
            arr1[0][j] = 1
            seen[(0, j)] = True
            stack.append((0, j))
            
        while stack: 
            (x, y) = stack.pop()
            for (i, j) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r, s = x + i, y + j
                if 0 <= r < n and 0 <= s < m and (r, s) not in seen: 
                    if heights[r][s] >= heights[x][y]:
                        seen[(r,s)] = True
                        arr1[r][s] = 1
                        stack.append((r, s))
        
        seen = {}
        stack = []
        for i in range(n):
            arr2[i][-1] = 1
            seen[(i, m - 1)] = True
            stack.append((i, m - 1))
        
        for j in range(m):
            arr2[-1][j] = 1
            seen[(n - 1, j)] = True
            stack.append((n - 1, j))
            
        while stack: 
            (x, y) = stack.pop()
            for (i, j) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r, s = x + i, y + j
                if 0 <= r < n and 0 <= s < m and (r, s) not in seen: 
                    if heights[r][s] >= heights[x][y]:
                        seen[(r, s)] = True
                        arr2[r][s] = 1
                        stack.append((r, s))
                        
        ans = []
        for i in range(n):
            for j in range(m):
                if arr1[i][j] + arr2[i][j] == 2: 
                    ans.append((i, j))
        
        return ans
        
        
class Solution2:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:    
        def helper(x, y, value): 
            if arr[x][y] < value:                  
                arr[x][y] += value 
                for i, j in (1, 0), (-1, 0), (0, 1), (0, -1):
                    r, s = x + i, y + j
                    if 0 <= r < n and 0 <= s < m:
                        if heights[r][s] >= heights[x][y]: 
                            helper(r, s, value)
       
        if not heights: 
            return []
        
        n, m = len(heights), len(heights[0])
        
        arr = [[0 for _ in range(m)] for _ in range(n)]
        
        for j in range(m): 
            helper(0, j, 1) 
            
        for i in range(n): 
            helper(i, 0, 1) 
        
        for j in range(m): 
            helper(n - 1, j, 2)
            
        for i in range(n): 
            helper(i, m - 1, 2)
        
        ans = []
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 3: 
                    ans.append((i, j))
        
        return ans
