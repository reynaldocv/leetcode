# https://leetcode.com/problems/matrix-cells-in-distance-order/

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        def helper(x, y):
            p = abs(x - rCenter)
            q = abs(y - cCenter)
            
            return p + q
        
        ans = [(i, j) for i in range(rows) for j in range(cols)]
        
        ans.sort(key = lambda item: (helper(item[0], item[1])))
        
        return ans 
