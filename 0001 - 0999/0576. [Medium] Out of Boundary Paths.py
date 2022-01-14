# https://leetcode.com/problems/out-of-boundary-paths/

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @cache 
        def helper(x, y, moves):
            if x == m or y == n or x < 0 or y < 0: 
                return 1
            
            if moves == 0: 
                return 0 
            
            ans = helper(x - 1, y, moves - 1)
            ans += helper(x, y - 1, moves - 1)
            ans += helper(x + 1, y, moves - 1)
            ans += helper(x, y + 1, moves - 1)
            
            return ans % MOD
        
        MOD = 10**9 + 7
        
        return helper(startRow, startColumn, maxMove)

        
