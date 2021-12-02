# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(root):
            if root: 
                self.ans.append(root.val)
                preorder(root.left)
                preorder(root.right)
        
        ans = self.ans = []
        preorder(root)
        return ans
