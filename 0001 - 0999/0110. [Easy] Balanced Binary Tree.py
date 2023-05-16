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
                (left, highLeft) = helper(node.left)
                (right, highRight) = helper(node.right)
                
                if left and right and abs(highLeft - highRight) <= 1: 
                    return (True, 1 + max(highLeft, highRight))
                    
                else: 
                    return (False, 0)
                
            else: 
                return (True, 0)
            
        return helper(root)[0]
            
       
                
                
