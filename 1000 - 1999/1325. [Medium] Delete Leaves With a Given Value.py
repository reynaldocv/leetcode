# https://leetcode.com/problems/delete-leaves-with-a-given-value/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def removeLeaf(root, target):
            if root: 
                root.left = removeLeaf(root.left, target)
                root.right = removeLeaf(root.right, target)
                if root.val == target and root.left == None and root.right == None: 
                    root = None       
                return root
            else: 
                return None
        
        return  removeLeaf(root, target)
        
