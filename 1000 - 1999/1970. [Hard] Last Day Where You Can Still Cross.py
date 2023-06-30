# https://leetcode.com/problems/last-day-where-you-can-still-cross/

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def helper(day):
            grid = [[0 for _ in range(col)] for _ in range(row)]

            stack = []
            
            for (x, y) in cells[: day]:
                grid[x - 1][y - 1] = 1

            for j in range(col):
                if grid[0][j] == 0:
                    stack.append((0, j))
                    
                    grid[0][j] = -1

            while stack:
                (x, y) = stack.pop(0)
                
                if x == row - 1:
                    return True
                    
                for r, s in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    p, q = x + r, y + s 
                    
                    if 0 <= p < row and 0 <= q < col and grid[p][q] == 0:
                        grid[p][q] = -1
                        
                        stack.append((p, q))

            return False

        start = 1 
        end = row*col
        
        while end - start > 1:
            middle = (end + start)//2
            
            if helper(middle):
                start = middle 
                
            else:
                end = middle

        return start

