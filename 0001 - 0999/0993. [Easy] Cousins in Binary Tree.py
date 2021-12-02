# https://leetcode.com/problems/cousins-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def levelFamily(root, level, father):
            if root:
                self.level[root.val] = (level, father)
                levelFamily(root.left, level + 1, root.val)
                levelFamily(root.right, level + 1, root.val)
                
        level = self.level = {}
        levelFamily(root, 0, None)
        if x in level and y in level:
            return level[x][0] == level [y][0] and level[x][1] != level [y][1]
        else:
            return False
                
