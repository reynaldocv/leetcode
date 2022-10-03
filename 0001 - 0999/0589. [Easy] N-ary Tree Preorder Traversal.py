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
        def helper(node):
            if node: 
                ans.append(node.val)
                
                for child in node.children: 
                    helper(child)
                    
        ans = []
        
        helper(root)
        
        return ans 
