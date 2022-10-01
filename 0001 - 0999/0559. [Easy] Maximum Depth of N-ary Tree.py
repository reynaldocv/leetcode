# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def helper(node):
            if node: 
                ans = 0 
                for child in node.children: 
                    ans = max(ans, helper(child))
                    
                return ans + 1 
            
            return 0 
            
        return helper(root)
