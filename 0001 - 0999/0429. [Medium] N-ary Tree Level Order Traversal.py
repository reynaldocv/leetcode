# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def helper(node, lvl):
            if node: 
                levels[lvl].append(node.val)
                
                for child in node.children: 
                    helper(child, lvl + 1)
                    
        levels = defaultdict(lambda: [])
        
        helper(root, 0)
        
        n = len(levels)
        
        return [levels[i] for i in range(n)]
             
        
