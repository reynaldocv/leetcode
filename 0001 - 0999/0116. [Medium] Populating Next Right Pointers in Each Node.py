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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def helper(node, lvl):
            if node: 
                node.next = level[lvl]
                
                level[lvl] = node
                
                helper(node.right, lvl + 1)
                helper(node.left, lvl + 1)
                
        level = defaultdict(lambda: None)
        
        helper(root, 0)
        
        return root
        
        
