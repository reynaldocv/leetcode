# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, maxValue):
            if root: 
                if root.val >= maxValue:
                    self.ans += 1
                maxValue = max(maxValue, root.val)
                helper(root.left, maxValue)
                helper(root.right, maxValue)
        
        self.ans = 0 
        helper(root, -inf)
        
        return self.ans
        
        
        
        
        
        
        
        
