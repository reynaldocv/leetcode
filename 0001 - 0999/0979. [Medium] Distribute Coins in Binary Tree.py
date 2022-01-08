# https://leetcode.com/problems/distribute-coins-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if node: 
                left = helper(node.left)
                right = helper(node.right)
                
                self.ans += abs(left) + abs(right)
                
                return node.val + left + right -1
            
            return 0 
        
        self.ans = 0 
        
        helper(root)
        
        return self.ans
        
