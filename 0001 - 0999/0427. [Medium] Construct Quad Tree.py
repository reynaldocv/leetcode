# https://leetcode.com/problems/construct-quad-tree/

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(x0, x1, y0, y1):
            val = {grid[i][j] for i in range(x0, x1) for j in range(y0, y1)}
            
            if len(val) == 1: 
                return Node(val.pop(), True, None, None, None, None)
            
            topLeft = helper(x0, (x0 + x1)//2, y0, (y0 + y1)//2)
            topRight = helper(x0, (x0 + x1)//2, (y0 + y1)//2, y1)
            bottomLeft = helper((x0 + x1)//2, x1, y0, (y0 + y1)//2)
            bottomRight = helper((x0 + x1)//2, x1, (y0 + y1)//2, y1)
            
            return Node(None, False, topLeft, topRight, bottomLeft, bottomRight)
        
        n = len(grid)
        
        return helper(0, n, 0, n)
