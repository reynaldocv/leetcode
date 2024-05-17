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
                left = helper(node.left)
                right = helper(node.right)
                
                if not left and not right and node.val == target: 
                    return None 
                
                else: 
                    return TreeNode(node.val, left, right)
                
            else: 
                return None 
    
        return helper(root)
