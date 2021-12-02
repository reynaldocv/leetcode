# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def route(root):
            if root: 
                route(root.right)
                root.val += self.aux
                self.aux = root.val
                route(root.left)
        
        self.aux = 0
        route(root)
        
        return root
        
