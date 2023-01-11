# https://leetcode.com/problems/construct-string-from-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def helper(node):
            if node: 
                ans = str(node.val)
                
                if node.right:
                    ans += "(" + helper(node.left) + ")(" + helper(node.right) + ")"
                
                elif node.left: 
                    ans += "(" + helper(node.left) + ")"
                    
                return ans 
            
            else: 
                return ""
            
        return helper(root)
                    
                    
                                        
                                       
                                    
        
