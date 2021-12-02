# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root, p, q):
            if root: 
                if root.val in [p.val, q.val]:
                    return root
                else: 
                    l = helper(root.left, p, q)
                    r = helper(root.right, p, q)
                    if l and r: 
                        return root
                    elif l: 
                        return l
                    else: 
                        return r
            else: 
                return None
            
        return helper(root, p, q)
