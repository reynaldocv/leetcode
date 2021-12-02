# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

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
        def route(root, level):
            if root: 
                root.next = nodeNext[level] if level in nodeNext else None
                nodeNext[level] = root
                route(root.right, level + 1)
                route(root.left, level + 1)
                    
        nodeNext = {}
        route(root, 0)
        
        return root
        
        
