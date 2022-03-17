# https://leetcode.com/problems/maximum-binary-tree-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def helper(node, val):
            if node: 
                if val >= node.val: 
                    return TreeNode(val, node, None)
                else:                     
                    node.right = helper(node.right, val)                    
                    return node
                    
            else: 
                return TreeNode(val)
        
        return helper(root, val)
    
