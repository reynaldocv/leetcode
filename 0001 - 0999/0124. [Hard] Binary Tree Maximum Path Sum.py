# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root: 
                elem = root.val                
                left = helper(root.left)
                right = helper(root.right)
                
                left = 0 if left < 0 else left
                right = 0 if right < 0 else right
                
                ans = root.val + max(left, right)
                
                self.ans = max(self.ans, ans, root.val + left + right)
                
                return ans
                
            else: 
                return 0
            
        self.ans = -inf
        helper(root)
        
        return self.ans
        
