# https://leetcode.com/problems/check-completeness-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def helper(node, idx):
            nonlocal counter, maxIdx
            if node: 
                counter += 1
                maxIdx = max(maxIdx, idx)
                
                helper(node.left, 2*idx)
                helper(node.right, 2*idx + 1)
                
        counter = 0
        maxIdx = 0 
        
        helper(root, 1)
        
        return counter == maxIdx
        
