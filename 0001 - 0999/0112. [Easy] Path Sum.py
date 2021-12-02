# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        
        def pathSum(root, value, target):
            if root:
                if root.left == None and root.right == None:                    
                    if value + root.val == target: 
                        return True
                else: 
                    l = pathSum(root.left, value + root.val, target)
                    r = pathSum(root.right, value + root.val, target)
                    return (l or r)
            return False
        
        return pathSum(root, 0, targetSum)
        
