# https://leetcode.com/problems/longest-univalue-path/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def paths(root):
            if root: 
                if root.left == None and root.right == None:                     
                    return root.val, 1 
                else:                     
                    Rval, Rh = paths(root.right)
                    Lval, Lh = paths(root.left)
                    if Rh == 0 and Lh == 0:
                        return root.val, 1
                    else:
                        Lh = Lh + 1 if Lval == root.val else 1
                        Rh = Rh + 1 if Rval == root.val else 1                       
                        self.ans = max(self.ans, Rh + Lh - 1)                        
                        return root.val, max(Rh, Lh) 
                 
            return inf, 0
        
        self.ans = 1
        paths(root)            
        
        return self.ans - 1
