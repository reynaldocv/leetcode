# https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return root
        elif root.val == val:
            return root
        else:
            left = self.searchBST(root.left, val)
            if left != None:
                return left
            else:
                right = self.searchBST(root.right, val)
                return right
            
                
        
