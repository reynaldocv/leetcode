# https://leetcode.com/problems/longest-univalue-path/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            nonlocal ans 
            if node: 
                (lVal, lLength) = helper(node.left)
                (rVal, rLength) = helper(node.right)

                lLength = lLength + 1 if lVal == node.val else 1   
                rLength = rLength + 1 if rVal == node.val else 1

                ans = max(ans, rLength + lLength - 1)

                return (node.val, max(rLength, lLength))
                
            else: 
                return (inf, 0)
        
        ans = 1
        
        helper(root)            
        
        return ans - 1
