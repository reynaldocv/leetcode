# https://leetcode.com/problems/evaluate-boolean-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if node: 
                if node.val in [0, 1]:
                    return node.val 
                elif node.val == 2: 
                    return helper(node.left) or helper(node.right)
                else: 
                    return helper(node.left) and helper(node.right)
                
        return helper(root)
