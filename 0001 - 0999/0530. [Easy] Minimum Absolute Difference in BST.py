# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def route(root):
            if root:
                self.arr.append(root.val)
                route(root.left)
                route(root.right)
        
        arr = self.arr = []
        route(root)
        arr.sort()
        ans = inf
        for i in range(1, len(arr)):
            ans = min(ans, arr[i] - arr[i - 1])
        return ans
        
