# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def helper(node):
            if node: 
                ans = 0 
                
                if low <= node.val <= high: 
                    ans = node.val
                
                return ans + helper(node.left) + helper(node.right)
                    
            else: 
                return 0 
            
        return helper(root)
            
