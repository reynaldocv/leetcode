# https://leetcode.com/problems/minimum-distance-between-bst-nodes/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def tourPreOrder(root):
            if root: 
                tourPreOrder(root.left)
                self.arr.append(root.val)                
                tourPreOrder(root.right)
        
        arr = self.arr = []
        tourPreOrder(root)
        n = len(arr)        
        ans = inf
        for i in range(n - 1, 0, -1):
            ans = min(ans, arr[i] - arr[i - 1])
        
        return ans
