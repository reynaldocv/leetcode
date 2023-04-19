# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def helper(left, right, node):
            nonlocal ans 
            
            if node: 
                ans = max(ans, left, right)
            
                helper(right + 1, 0, node.left)
                helper(0, left + 1, node.right)
                
        ans = 0 
        
        helper(0, 0, root)
        
        return ans 
        
