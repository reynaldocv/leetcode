# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(node, value):
            nonlocal ans
            if node: 
                if not node.left and not node.right: 
                    ans += int(10*value + node.val)
                    
                helper(node.left, 10*value + node.val)
                helper(node.right, 10*value + node.val)
            
        ans = 0 
        
        helper(root, 0)
        
        return ans 
