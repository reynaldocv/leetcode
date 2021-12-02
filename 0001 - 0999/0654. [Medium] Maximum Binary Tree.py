# https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def maximum(nums):
            ans = (-1, -1)
            for i in range(len(nums)):
                ans = max(ans, (nums[i], i))
            return ans
        
        def createBT(nums):
            if len(nums) == 0:
                return None
            else: 
                value, idx = maximum(nums)
                ans = TreeNode(value)
                ans.left = createBT(nums[:idx])
                ans.right = createBT(nums[idx + 1:])
                return ans
        
        ans = createBT(nums)
        return ans
                
        
