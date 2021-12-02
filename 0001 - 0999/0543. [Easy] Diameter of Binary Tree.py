# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def hight(root):
            if root == None: 
                return 0
            else: 
                h1 = hight(root.left)
                h2 = hight(root.right)
                self.diameter = max(self.diameter, h1 + h2)
                return 1 + max(h1, h2)
        
        self.diameter = 0
        hight(root)
        return self.diameter
