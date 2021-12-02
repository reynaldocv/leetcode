# https://leetcode.com/problems/binary-tree-pruning/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def prune(root):
            if root: 
                root.left = prune(root.left)
                root.right = prune(root.right)
                
                if not root.left and not root.right and root.val == 0: 
                    root = None
                
                return root
            
            return None
        
        return prune(root)
        
                    
                    
