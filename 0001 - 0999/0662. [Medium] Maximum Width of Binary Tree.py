# https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root, idx, lvl):
            if root: 
                left[lvl] = min(left.get(lvl, inf), idx)
                right[lvl] = max(right.get(lvl, -inf), idx)
                helper(root.left, idx*2, lvl + 1)
                helper(root.right, idx*2 + 1, lvl + 1)
            
        left = {}
        right = {}
        helper(root, 0, 0)
        
        ans = 0 
        for key in left: 
            ans = max(ans, right[key] - left[key] + 1)
            
        return ans
        
