# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            nonlocal ans 
            
            if node: 
                left = helper(node.left)
                right = helper(node.right)
                
                left = 0 if left < 0 else left 
                right = 0 if right < 0 else right
                
                ans = max(ans, node.val + right + left)
                
                return node.val + max(left, right)
            
            else: 
                return 0 
            
        ans = -inf 
        
        helper(root)
        
        return ans 
        
        
