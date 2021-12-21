# https://leetcode.com/problems/cherry-pickup-ii/

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        @cache
        def helper(row, col1, col2):
            if not(0 <= col1 < n and 0 <= col2 < n):
                return -inf 
            
            ans = grid[row][col1] + grid[row][col2]

            if row != m - 1:
                aux = 0 
                for newCol1 in [col1, col1 + 1, col1 - 1]:
                    for newCol2 in [col2, col2 + 1, col2 - 1]:
                        if newCol1 != newCol2:
                            aux = max(aux, helper(row + 1, newCol1, newCol2))

                ans += aux

            return ans

        m, n = len(grid), len(grid[0])
           
        return helper(0, 0, n - 1)
                            
