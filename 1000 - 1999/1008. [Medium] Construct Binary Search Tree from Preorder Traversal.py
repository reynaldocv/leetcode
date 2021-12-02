# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def create(nums):
            if len(nums) == 0: 
                return None
            else: 
                val = nums[0]
                idx = 0
                for i in range(1, len(nums)):
                    if nums[i] < val: 
                        idx = i
                    else: 
                        break
                ans = TreeNode(val)
                ans.left = create(nums[1:idx + 1])
                ans.right = create(nums[idx + 1:])
                return ans
            
        return create(preorder)
