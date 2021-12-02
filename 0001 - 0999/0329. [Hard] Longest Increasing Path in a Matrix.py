# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @cache
        def helper(x, y):
            ans = 1
            for (i, j) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r, s = x + i, y + j
                if 0 <= r < n and 0 <= s < m: 
                    if matrix[x][y] < matrix[r][s]:
                        ans = max(ans, 1 + helper(r, s))
            return ans
        
        n, m = len(matrix), len(matrix[0])    
        ans = 0 
        for i in range(n):
            for j in range(m):
                ans = max(ans, helper(i, j))
        
        return ans
        
    
        
        
        
        
        
        
