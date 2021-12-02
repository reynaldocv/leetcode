# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def numbersToLeaf(root, val):
            if root: 
                if root.left == None and root.right == None: 
                    num = int(val + str(root.val))
                    return num
                else: 
                    return numbersToLeaf(root.left, val + str(root.val)) + numbersToLeaf(root.right, val + str(root.val))
            else: 
                return 0
                    
        return numbersToLeaf(root, "")
        
                    
            
        
