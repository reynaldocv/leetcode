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
        def helper(root):
            if root: 
                helper(root.left)
                inorder.append(root)
                helper(root.right)
            
        inorder = []        
        helper(root)
        
        wrongNodes = []
        
        for (i, root)  in enumerate(sorted(inorder, key = lambda item: item.val)):
            if inorder[i].val != root.val:
                wrongNodes.append(root)
            
        wrongNodes[0].val, wrongNodes[1].val = wrongNodes[1].val, wrongNodes[0].val
        
        
        
