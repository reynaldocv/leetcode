# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(root, maxVal, minVal):
            if not root: 
                return maxVal -  minVal
            else: 
                maxVal = max(maxVal, root.val)
                minVal = min(minVal, root.val)
                
                left = helper(root.left, maxVal, minVal)
                right = helper(root.right, maxVal, minVal)
                
                return max(left, right)
            
        if not root: 
            return 0 
        
        return helper(root, root.val, root.val)
                
        
        
