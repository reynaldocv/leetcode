# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def helper(value, node):
            nonlocal ans 
           
            if node: 
                value = 2*value + node.val
                
                if not node.left and not node.right: 
                    ans += value
                    
                helper(value, node.left)
                helper(value, node.right)
                
        ans = 0 
        
        helper(0, root)
        
        return ans 
            
