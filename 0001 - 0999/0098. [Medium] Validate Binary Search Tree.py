# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, lower, upper):
            if node: 
                if lower < node.val < upper: 
                    left = helper(node.left, lower, node.val) 
                    right = helper(node.right, node.val, upper)
                    
                    return left and right
                
                else: 
                    return False 
                
            return True 
        
        return helper(root, -inf, inf)
            
        
    
        
        
        
