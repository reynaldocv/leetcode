# https://leetcode.com/problems/even-odd-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        def helper(root, odd, lvl):
            if root: 
                if (root.val % 2 == odd):
                    lvls[lvl].append(root.val)
                    left = helper(root.left, (odd + 1) % 2, lvl + 1)
                    right = helper(root.right, (odd + 1) % 2, lvl + 1)
                    return True if left and right else False
                else: 
                    return False
            else: 
                return True
            
            
        lvls = defaultdict(lambda: []) 
        
            
        if helper(root, 1, 0):
            for lvl in lvls: 
                if lvl % 2 == 0: 
                    if lvls[lvl] != sorted(set(lvls[lvl])):
                        return False
                else: 
                    if lvls[lvl] != sorted(set(lvls[lvl]), reverse = True):
                        return False
            return True
        else: 
            return False
