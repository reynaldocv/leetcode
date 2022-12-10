# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if node: 
                node.val += helper(node.left) + helper(node.right)
                
                return node.val
            
            return 0 
                
        def collaborator(node):
            nonlocal ans            
            if node: 
                ans = max(ans, node.val*(aSum - node.val))
                
                collaborator(node.left)
                collaborator(node.right)
            
        MOD = 10**9 + 7
        ans = 0       
        
        aSum = helper(root)        
        
        collaborator(root)        
        
        return ans % MOD
