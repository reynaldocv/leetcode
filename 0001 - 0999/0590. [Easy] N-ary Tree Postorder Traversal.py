# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def subpostorder(root):
            if root: 
                if root.children: 
                    for child in root.children: 
                        subpostorder(child)
                self.ans.append(root.val)
                
        self.ans = []
        subpostorder(root)
        return self.ans
