# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrder(root):
            if root: 
                inOrder(root.left)
                self.count += 1
                if self.count == k:
                    self.ans = root.val
                inOrder(root.right)
        
        self.count = 0
        self.ans = 0
        inOrder(root)
        
        return self.ans
