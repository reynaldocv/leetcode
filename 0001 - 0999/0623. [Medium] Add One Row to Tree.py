# https://leetcode.com/problems/add-one-row-to-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def helper(root, h):
            if h > 1:
                if root: 
                    root.left = helper(root.left, h - 1)
                    root.right = helper(root.right, h - 1)               
            elif h == 1:
                if root: 
                    root.left = TreeNode(val, root.left, None)
                    root.right = TreeNode(val, None, root.right)
            
            return root
            
        newTree = TreeNode(0, root, None)
        
        helper(newTree, depth)
    
        return newTree.left
        
