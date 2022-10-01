# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def hight(root):
            if root == None: 
                return 0
            
            else: 
                h1 = hight(root.left)
                h2 = hight(root.right)
        
                self.diameter = max(self.diameter, h1 + h2)
                
                return 1 + max(h1, h2)
        
        self.diameter = 0
        
        hight(root)
        
        return self.diameter

class Solution2:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if node: 
                leftDiameter, leftHigh = helper(node.left)
                rightDiameter, rightHigh = helper(node.right)
                
                return max(leftDiameter, rightDiameter, leftHigh + rightHigh), max(leftHigh, rightHigh) + 1
            
            return 0, 0 
        
        return helper(root)[0]
        
