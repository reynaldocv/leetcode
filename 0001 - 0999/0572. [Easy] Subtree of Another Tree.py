# https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(node):
            if node: 
                if collaborator(node, subRoot):
                    return True 
                
                return helper(node.left) or helper(node.right)
                
            else:
                return False 
        
        def collaborator(node, tmp):
            if node and tmp: 
                if node.val == tmp.val:
                    return collaborator(node.left, tmp.left) and collaborator(node.right, tmp.right)
                
                else: 
                    return False 
            
            elif not node and not tmp: 
                return True 
            
            else: 
                return False 
        
        return helper(root)
