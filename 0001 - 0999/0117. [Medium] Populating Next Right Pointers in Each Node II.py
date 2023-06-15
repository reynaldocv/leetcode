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
        def helper(node, lvl):
            if node: 
                helper(node.right, lvl + 1)
            
                node.next = seen[lvl]
                seen[lvl] = node
                
                helper(node.left, lvl + 1)
               
        seen = defaultdict(lambda: None)
        
        helper(root, 0)
        
        return root
        
        
