# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            nonlocal ans 
            
            if node: 
                left = helper(node.left)
                right = helper(node.right)
                
                ans = max(ans, left + right)
                
                return 1 + max(left, right)
                
            else: 
                return 0 
            
        ans = 0 
        
        helper(root)
        
        return ans 
        
