# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pval = p.val
        qval = q.val 
        if pval > qval: 
            pval, qval = qval, pval
        while root: 
            if pval < root.val < qval:
                return root 
            elif pval == root.val or qval == root.val:
                return root 
            else: 
                if pval < root.val and qval < root.val:
                    root = root.left
                else: 
                    root = root.right
        return None
        
