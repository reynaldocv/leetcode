# https://leetcode.com/problems/construct-string-from-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: TreeNode) -> str:
        def tour(root):
            if root: 
                self.ans += str(root.val)
                if root.left:
                    self.ans += "("
                    tour(root.left)
                    self.ans += ")"
                if root.right:
                    if root.left == None: 
                        self.ans += "()"
                    self.ans += "("                        
                    tour(root.right)
                    self.ans += ")"
                    
        self.ans = ""
        tour(root)
        return self.ans
