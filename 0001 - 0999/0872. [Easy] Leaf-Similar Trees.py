# https://leetcode.com/problems/leaf-similar-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def helper(node, arr):
            if node: 
                helper(node.left, arr)
                
                if not node.left and not node.right: 
                    arr.append(node.val)
        
                helper(node.right, arr)
            
        arr1, arr2 = [], []
        
        helper(root1, arr1)
        helper(root2, arr2)
        
        return arr1 == arr2
