# https://leetcode.com/problems/sum-of-left-leaves/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper(node, isLeft):
            nonlocal ans
            
            if node: 
                if not node.left and not node.right and isLeft: 
                    ans += node.val 
                    
                helper(node.left, True)
                helper(node.right, False)

        ans = 0 
        
        helper(root, False)
        
        return ans 
        
