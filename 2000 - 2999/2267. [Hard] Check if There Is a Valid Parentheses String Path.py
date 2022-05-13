# https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        @cache
        def helper(i, j, cnt): 
            if i == m - 1 and j == n - 1: 
                return cnt == 0 
            
            for (r, s) in [(i + 1, j), (i, j + 1)]: 
                if 0 <= r < m and 0 <= s < n: 
                    if grid[r][s] == '(': 
                        tmp = cnt + 1
                    else: 
                        tmp = cnt - 1
                    
                    if tmp >= 0 and helper(r, s, tmp): 
                        return True 
                    
            return False 
        
        m, n = len(grid), len(grid[0])
        
        if grid[0][0] == "(":            
            return helper(0, 0, 1)
        else: 
            return False
