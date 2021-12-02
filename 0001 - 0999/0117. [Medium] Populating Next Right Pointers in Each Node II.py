# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def helper(root, lvl):
            if root: 
                helper(root.right, lvl + 1)
                if lvl in level: 
                    root.next = level[lvl]
                level[lvl] = root
                helper(root.left, lvl + 1)
        
        level = {}
        helper(root, 0)
        
        return root
        
        
