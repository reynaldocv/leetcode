# https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        @cache
        def helper(x, y, cnt):
            if x == m - 1 and y == n - 1:
                return cnt == 0 
            else: 
                for (r, s) in [(x + 1, y), (x, y + 1)]:
                    if 0 <= r < m and 0 <= s < n: 
                        cnt2 = cnt                        
                        if grid[r][s] == "(":
                            cnt2 += 1 
                        else:
                            cnt2 -= 1 
                            
                        if cnt2 >= 0 and helper(r, s, cnt2):
                            return True 
                        
                return False 
            
        m, n = len(grid), len(grid[0])
            
        if grid[0][0] == "(":
            return helper(0, 0, 1)
        else: 
            return False 
            
