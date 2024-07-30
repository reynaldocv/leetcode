# https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def helper(node, value):
            if not node: 
                return None
            
            value -= node.val
            
            if node.left == None and node.right == None: 
                if value > 0:
                    return None
            
                else: 
                    return node
                
            else: 
                node.left = helper(node.left, value)
                node.right = helper(node.right, value)

                if node.left == None and node.right == None: 
                    return None
                else: 
                    return node

        return helper(root, limit)
