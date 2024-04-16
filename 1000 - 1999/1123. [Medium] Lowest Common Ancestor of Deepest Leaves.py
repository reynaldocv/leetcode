# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if not node: 
                return (0, None)  
            
            else: 
                (left, nodeLeft) = helper(node.left)
                (right, nodeRight) = helper(node.right)
                
                if left == right: 
                    return (1 + left, node)
                
                elif left > right: 
                    return (1 + left, nodeLeft)
                
                else: 
                    return (1 + right, nodeRight)
                
        return helper(root)[1]
