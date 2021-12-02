# https://leetcode.com/problems/sum-of-left-leaves/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def leftLeaves(root, left):
            if root:
                if root.left == None and root.right == None: 
                    if left == True:
                        self.ans += root.val
                else:
                    leftLeaves(root.left, True)
                    leftLeaves(root.right, False)
        self.ans = 0
        leftLeaves(root, "False")
        return self.ans
        
                
        
