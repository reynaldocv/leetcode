# https://leetcode.com/problems/n-ary-tree-preorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        def subpreorder(root):
            if root:
                self.ans.append(root.val)
                if root.children != None:
                    for child in root.children:
                        subpreorder(child)
                
        self.ans = []
        subpreorder(root)
        return self.ans
