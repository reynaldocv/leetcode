# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def mirror(root1, root2):
            if root1 == None and root2 == None: 
                return True
            if root1 and root2: 
                if root1.val != root2.val: 
                    return False
                else:                     
                    l = mirror(root1.left, root2.right)
                    r = mirror (root1.right, root2.left)
                    return (l and r)
            return False
        
        return mirror(root.left, root.right)
        
