# https://leetcode.com/problems/univalued-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if node: 
                seen.add(node.val)
                
                helper(node.left)
                helper(node.right)
        
        seen = set()
        
        helper(root)
        
        return len(seen) == 1
        
