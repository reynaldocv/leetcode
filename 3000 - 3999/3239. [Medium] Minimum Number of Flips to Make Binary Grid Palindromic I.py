# https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        def helper(arr):
            l = len(arr)
            
            ans = 0 
            
            for i in range(l//2):
                if arr[i] != arr[l - i - 1]:
                    ans += 1 
                    
            return ans 
        
        m, n = len(grid), len(grid[0])
        
        ans = [0, 0]
        
        for row in grid: 
            ans[0] += helper(row)
        
        tGrid = [[grid[i][j] for i in range(m)] for j in range(n)]
        
        for row in tGrid: 
            ans[1] += helper(row)
            
        return min(ans)
                  
                 
