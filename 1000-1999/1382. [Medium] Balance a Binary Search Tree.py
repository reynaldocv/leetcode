# https://leetcode.com/problems/balance-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if root: 
                inorder(root.left)
                arr.append(root.val)
                inorder(root.right)
        
        def createBST(arr):
            if arr: 
                n = len(arr)//2
                root = TreeNode(arr[n])
                root.left = createBST(arr[:n])
                root.right = createBST(arr[n + 1:])
            else: 
                root = None
            
            return root
            
        arr = []
        inorder(root)
        
        return createBST(arr)
