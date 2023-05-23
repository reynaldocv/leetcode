# https://leetcode.com/problems/recover-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(node):
            if node: 
                helper(node.left)
                
                inorder.append(node)                
                tmp.append(node.val)
                
                helper(node.right)
        
        arr = []
        tmp = []
        
        helper(root)
        
        tmp.sort()
        
        n = len(arr)
        
        for i in range(n):
            if inorder[i].val != tmp[i]: 
                inorder[i].val = tmp[i]
                
                
        
        
        
