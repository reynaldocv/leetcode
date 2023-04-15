# https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(arr):
            if arr: 
                maxElem = (-1, -1)
                
                for (i, num) in enumerate(arr):
                    maxElem = max(maxElem, (num, i))
                    
                (elem, idx) = maxElem
                    
                ans = TreeNode(elem)
                
                ans.left = helper(arr[: idx])
                ans.right = helper(arr[idx + 1: ])
                
                return ans 
            
            else: 
                return None 
                
        return helper(nums)
