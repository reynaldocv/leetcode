# https://leetcode.com/problems/find-bottom-left-tree-value/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(root, level, dic):
            if root: 
                dfs(root.right, level + 1, dic)
                dic[level] = root.val
                dfs(root.left, level + 1, dic)
                
        dic = {}
        dfs(root, 0, dic)
        return dic[len(dic) - 1]
