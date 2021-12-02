https://leetcode.com/problems/convert-bst-to-greater-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def route(root):
            if root: 
                route(root.right)                
                root.val += self.val
                self.val = root.val 
                route(root.left)
                
        
        self.val = 0
        route(root)
        
        return root
        
