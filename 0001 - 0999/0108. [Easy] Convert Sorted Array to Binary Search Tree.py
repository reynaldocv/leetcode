# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def createBST(nums):
            n = len(nums)
            if n > 0:
                idx = n//2
                root = TreeNode(nums[idx], None, None)
                root.left = createBST(nums[:idx])                
                root.right = createBST(nums[idx + 1:])
                return root
            return None
        
        ans = createBST(nums)
        return ans
        
