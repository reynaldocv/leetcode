# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def sameTree(p, q):
            if p == None and q == None: 
                return True
            elif p == None or q == None:
                return False
            else: 
                if p.val != q.val:
                    return False
                else: 
                    l = sameTree(p.left, q.left)
                    r = sameTree(p.right, q.right)
                    return (l and r)
        
        return sameTree(p, q)
                    
        
