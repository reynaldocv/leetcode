# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        def route(root, level, levels):
            if root: 
                levels[level] = levels.get(level, [])
                levels[level].append(root.val)
                route(root.left, level + 1, levels)
                route(root.right, level + 1, levels)
        
        levels = {}
        route(root, 0, levels)
        ans = []
        for i in range(len(levels) - 1, -1, -1):
            ans.append(levels[i])
        
        return ans
