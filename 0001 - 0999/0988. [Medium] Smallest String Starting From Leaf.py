# https://leetcode.com/problems/smallest-string-starting-from-leaf/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def helper(node, word):
            nonlocal ans 
            
            if node: 
                char = chr(ord("a") + node.val) 
                if not node.left and not node.right: 
                    ans = min(ans, char + word)
                    
                helper(node.left, char + word)
                helper(node.right, char + word)
                
        ans = chr(ord("z") + 1)
        
        helper(root, "")
        
        return ans 
        
        
            
            
            
            
