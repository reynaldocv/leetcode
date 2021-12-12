# https://leetcode.com/problems/smallest-string-starting-from-leaf/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def helper(root, aux):
            nonlocal ans
            if root: 
                char = chr(root.val + ord("a"))
                if not root.left and not root.right:
                    aux += char
                    ans = min(ans, aux[::-1])
                
                helper(root.left, aux + char)
                helper(root.right, aux + char)
                
        ans = chr(255)
        
        helper(root, "")
        
        return ans
            
            
            
            
            
