# https://leetcode.com/problems/univalued-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def UnivalTree(root, val):
            if root == None:
                return True
            else:
                return (root.val == val) and UnivalTree(root.left, val) and UnivalTree(root.right, val)
        
        if root == None:
            return True
        else:
            return UnivalTree(root, root.val)
            
        
