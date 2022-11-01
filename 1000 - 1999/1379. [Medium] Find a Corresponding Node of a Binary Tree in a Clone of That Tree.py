# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def helper(original, cloned):
            if original: 
                if original == target: 
                    return cloned
                
                left = helper(original.left, cloned.left)
                if not left: 
                    return helper(original.right, cloned.right)
                    
                return left
            else: 
                return None

        return helper(original, cloned)               
                    
                    
            
