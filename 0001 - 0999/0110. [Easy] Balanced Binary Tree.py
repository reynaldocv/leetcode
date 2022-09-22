# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if node: 
                (left, leftBool) = helper(node.left)
                (right, rightBool) = helper(node.right)
                
                if leftBool and rightBool: 
                    if abs(left - right) <= 1: 
                        return (1 + max(left, right), True)
                    else: 
                        return (0, False)
                else: 
                    return (0, False)                 
            else: 
                return (0, True)
                
        return helper(root)[1]
       
                
                
