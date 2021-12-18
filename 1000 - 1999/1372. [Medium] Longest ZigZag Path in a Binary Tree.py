# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def helper(root, length, right):
            nonlocal ans
            if root: 
                ans = max(ans, length)
                if right: 
                    helper(root.left, length + 1, not right)
                    helper(root.right, 1, right)
                else: 
                    helper(root.right, length + 1, not right)
                    helper(root.left, 1, right)
        
        ans = 0
        
        helper(root, 0, True)
        
        return ans
        
        
