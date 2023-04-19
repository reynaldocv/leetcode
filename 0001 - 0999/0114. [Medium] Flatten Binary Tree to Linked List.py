# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(node):
            if node: 
                arr.append(node)
                
                helper(node.left)
                helper(node.right)
            
        if not root: 
            return None 
        
        arr = []
        
        helper(root)
        
        n = len(arr)
        
        for i in range(n - 1):
            arr[i].right = arr[i + 1]
            arr[i].left = None 
            
        arr[-1].left = None 
        arr[-1].right = None 
        
        
            
