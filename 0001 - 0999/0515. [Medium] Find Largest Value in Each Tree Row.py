# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root, lvl):
            if root: 
                seen[lvl] = max(seen.get(lvl, -inf), root.val)
                helper(root.left, lvl + 1)
                helper(root.right, lvl + 1)
        
        seen = {}
        helper(root, 0)
        
        return [*seen.values()]
        
