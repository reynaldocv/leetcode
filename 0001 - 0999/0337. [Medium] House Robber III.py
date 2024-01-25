# https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache 
        def helper(node, visit):
            if node: 
                if visit: 
                    ans = helper(node.left, False) + helper(node.right, False)
                    
                else:
                    ans = node.val + helper(node.left, True) + helper(node.right, True)
                    
                    ans = max(ans, helper(node.left, False) + helper(node.right, False))  
                    
                return ans 
                
            else: 
                return 0 
            
            
        return helper(root, False)        
