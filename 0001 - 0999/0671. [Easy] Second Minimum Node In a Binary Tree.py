# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def tour(root):
            if root: 
                self.ans.add(root.val)
                tour(root.left)
                tour(root.right)
                
        ans = self.ans = set([])
        tour(root)
        ans = list(ans)
        ans.sort()
        if len(ans) <= 1: 
            return -1
        else: 
            return ans[1]
        
                
