# https://leetcode.com/problems/minimum-moves-to-capture-the-queen/

class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:        
        for (r, s) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            (x, y) = (a, b)

            for _ in range(8):
                x, y = x + r, y + s

                if x == c and y == d: 
                    break 

                if x == e and y == f: 
                    return 1 
        
        for (r, s) in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            (x, y) = (c, d)

            for _ in range(8):
                x, y = x + r, y + s

                if x == a and y == b: 
                    break 

                if x == e and y == f: 
                    return 1 
                    
        return 2
