# https://leetcode.com/problems/add-one-row-to-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def helper(node, lvl):
            if node: 
                if lvl == depth: 
                    node.left = TreeNode(val, node.left, None)
                    node.right = TreeNode(val, None, node.right)
                    
                else: 
                    node.left = helper(node.left, lvl + 1)
                    node.right = helper(node.right, lvl + 1)
                    
                return node
                    
            else: 
                return None
        
        if depth == 1: 
            return TreeNode(val, root, None)
        
        else:         
            return helper(root, 2)
        
