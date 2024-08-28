# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0]) 
        
        heap = []
        
        for i in range(m):
            for j in range(n):
                heappush(heap, (matrix[i][j], i, j))
                
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        ans = 0 
        
        while heap: 
            (value, x, y) = heappop(heap)
            
            tmp = 0 
            
            for (r, s) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                p, q = x + r, y + s
                
                if 0 <= p < m and 0 <= q < n: 
                    if matrix[p][q] < value: 
                        tmp = max(tmp, dp[p][q])
                        
            dp[x][y] = tmp + 1
            
            ans = max(ans, dp[x][y])
            
        return ans 
            
        
    
        
        
        
        
        
        
