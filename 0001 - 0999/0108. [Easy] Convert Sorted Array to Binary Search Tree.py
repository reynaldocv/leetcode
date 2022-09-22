# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(arr):
            if arr: 
                n = len(arr)
                mid = n//2
                
                return TreeNode(arr[mid], helper(arr[: mid]), helper(arr[mid + 1: ]))
                
            else: 
                return None
            
        return helper(nums)
        
