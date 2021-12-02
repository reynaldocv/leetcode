# https://leetcode.com/problems/deepest-leaves-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def high(root):
            if root:
                return 1 + max(high(root.left), high(root.right))
            return 0
            
        def sumDeepestLeaves(root, h):
            if root:
                aux = 0
                if h == 0:
                    aux = root.val
                else:
                    aux += sumDeepestLeaves(root.left, h - 1)
                    aux += sumDeepestLeaves(root.right, h - 1)
                return aux            
            return 0  
            
        h = high(root)
        return sumDeepestLeaves(root, h - 1)
