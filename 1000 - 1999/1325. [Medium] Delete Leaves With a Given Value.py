# https://leetcode.com/problems/delete-leaves-with-a-given-value/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def helper(node):
            if node:                 
                node.left = helper(node.left)
                node.right = helper(node.right)
                
                if node.left == None and node.right == None and node.val == target: 
                    return None 
                
                return node
            
            else: 
                return None
        
        return helper(root)
