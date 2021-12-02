# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def  balanced(root):
            if not root:
                return 0, True 
            else: 
                h1, b1 = balanced(root.left) 
                h2, b2 = balanced(root.right)
                h1 += 1
                h2 += 1
                b3 = True if abs(h1 - h2) <= 1 else False 
                return max(h1, h2), b1 and b2 and b3
        
        return balanced(root)[1]
       
                
                
