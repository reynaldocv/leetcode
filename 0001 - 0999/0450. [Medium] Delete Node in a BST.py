# https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findMinNode(root):            
            while root.left: 
                root = root.left
            
            return root
        
        def delete(root, key):
            if not root: 
                return None
            if key < root.val: 
                root.left = delete(root.left, key)
            elif key > root.val: 
                root.right = delete(root.right, key)
            else: 
                if not root.left: 
                    root = root.right
                elif not root.right: 
                    root = root.left
                else: 
                    successor = findMinNode(root.right)
                    root.val = successor.val
                    root.right = delete(root.right, successor.val)
            return root
        
        return delete(root, key)
