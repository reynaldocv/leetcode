https://leetcode.com/problems/convert-bst-to-greater-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            nonlocal aSum       
            
            if node:                 
                helper(node.right)                
                
                node.val += aSum                 
                aSum = node.val
                
                helper(node.left)
                
            else: 
                return 0 
            
        aSum = 0 
            
        helper(root)
        
        return root
        
