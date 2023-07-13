# https://leetcode.com/problems/find-bottom-left-tree-value/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def helper(node, lvl):
            if node: 
                helper(node.right, lvl + 1)

                seen[lvl] = node.val 
                
                helper(node.left, lvl + 1)
        
        seen = {}
        
        helper(root, 0)
        
        return seen[len(seen) - 1]
        
        
