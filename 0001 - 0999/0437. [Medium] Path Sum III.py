# https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def paths(root, arr, targetSum):
            if root: 
                arr.append(root.val)
                for i in range(len(arr)):
                    if sum(arr[i:]) == targetSum: 
                        self.ans += 1
                paths(root.left, arr, targetSum)
                paths(root.right, arr, targetSum)
                arr.pop()
        
        self.ans = 0
        paths(root, [], targetSum)
        
        return self.ans
        
