# https://leetcode.com/problems/count-complete-tree-nodes/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def countTotalNodes(root):
            lh = 0
            cur = root        
            while cur:
                cur, lh = cur.left, lh + 1

            rh = 0
            cur = root
            while cur:
                cur, rh = cur.right, rh + 1

            if rh == lh: 
                return (2**lh - 1)
            else: 
                return 1 + countTotalNodes(root.left) + countTotalNodes(root.right)
        
        return countTotalNodes(root)

