# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def postorder(root):
            if root: 
                postorder(root.left)
                postorder(root.right)
                self.ans.append(root.val)
        
        ans = self.ans = []
        postorder(root)
        return ans
        
