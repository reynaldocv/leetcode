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
                left = helper(node.left)
                right = helper(node.right)
                node.val += left + right
                return node.val
            else: 
                return 0 
            
        def collaborator(node):
            nonlocal ans
            if node: 
                if node.left: 
                    tmp = aSum - node.left.val
                    ans = max(ans, tmp*node.left.val)
                if node.right: 
                    tmp = aSum - node.right.val
                    ans = max(ans, tmp*node.right.val)
                collaborator(node.left)
                collaborator(node.right)
            
        MOD = 10**9 + 7
        aSum = helper(root)        
        
        ans = 0        
        collaborator(root)        
        
        return ans % MOD
