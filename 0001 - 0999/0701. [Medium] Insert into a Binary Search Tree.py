# https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def helper(node, val):
            if node: 
                if node.val < val: 
                    node.right = helper(node.right, val)
                    
                else: 
                    node.left = helper(node.left, val)
                    
                return node
            else: 
                return TreeNode(val)
    
        return helper(root, val)
        
