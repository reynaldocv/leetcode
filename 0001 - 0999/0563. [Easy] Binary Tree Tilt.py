#https://leetcode.com/problems/binary-tree-tilt/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if node: 
                left, leftSum = helper(node.left)
                right, rightSum = helper(node.right)
                
                tmp = abs(left - right)
                
                return left + right + node.val, leftSum + rightSum + tmp
            
            return 0, 0
        
        return helper(root)[1]

class Solution2:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if node: 
                left = helper(node.left)
                right = helper(node.right)
                
                self.ans += abs(left - right)
                
                return left + right + node.val
            
            return 0 
        
        self.ans = 0 
        
        helper(root)
        
        return self.ans

        
        
