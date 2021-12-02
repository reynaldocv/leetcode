# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inOrder(root):
            if root: 
                inOrder(root.left)
                arr.append(root.val)
                inOrder(root.right)
        
        arr = []
        inOrder(root)
        n = len(arr)
        for i in range(1, n):
            if arr[i] <= arr[i - 1]:
                return False
        
        return True
            
        
    
        
        
        
