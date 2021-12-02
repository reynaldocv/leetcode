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
        def helper(root, lvl):
            if root: 
                seen[lvl].append(root.val)
                if root.children: 
                    for child in root.children: 
                        helper(child, lvl + 1)
                        
        seen = defaultdict(list)
        helper(root, 0)
        
        return [*seen.values()]
                    
        
