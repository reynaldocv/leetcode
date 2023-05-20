# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node):
            if node: 
                if node == p or node == q:                     
                    return node
                
                else:                     
                    left = helper(node.left)
                    right = helper(node.right)

                    if left and right: 
                        return node

                    elif left: 
                        return left 

                    else: 
                        return right 
            else: 
                return None 
                
        return helper(root)
        
