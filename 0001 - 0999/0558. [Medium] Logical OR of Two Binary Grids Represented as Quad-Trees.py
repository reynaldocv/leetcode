# https://leetcode.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/

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
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        def helper(qt1, qt2):
            if qt1.isLeaf: 
                return qt1 if qt1.val else qt2
            
            if qt2.isLeaf: 
                return qt2 if qt2.val else qt1
            
            tL = helper(qt1.topLeft, qt2.topLeft)
            tR = helper(qt1.topRight, qt2.topRight)
            bL = helper(qt1.bottomLeft, qt2.bottomLeft)
            bR = helper(qt1.bottomRight, qt2.bottomRight)
            
            if tL.isLeaf and tR.isLeaf and bL.isLeaf and bR.isLeaf: 
                if tL.val == tR.val == bL.val == bR.val: 
                    return Node(tL.val, True)
                
            return Node(None, False, tL, tR, bL, bR)
    
        return helper(quadTree1, quadTree2)
            

        
