# https://leetcode.com/problems/cousins-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def helper(node, lvl, parent):
            if node: 
                seen[node.val] = (lvl, parent)
                
                helper(node.left, lvl + 1, node.val)
                helper(node.right, lvl + 1, node.val)
                
        seen = {}
        
        helper(root, 0, -1)
        
        if x not in seen and y not in seen: 
            return False 
        
        return seen[x][0] == seen[y][0] and seen[x][1] != seen[y][1]
        
        
                
        
        
        
        
