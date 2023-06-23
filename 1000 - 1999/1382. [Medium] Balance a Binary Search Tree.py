# https://leetcode.com/problems/balance-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def helper(node):
            if node: 
                helper(node.left)
                
                arr.append(node.val)
                
                helper(node.right)
                
        def collaborator(nums):
            if nums: 
                idx = len(nums)//2
                
                ans = TreeNode(nums[idx])
                
                ans.left = collaborator(nums[: idx])
                ans.right = collaborator(nums[idx + 1: ])
                
                return ans
                
            else: 
                return None 
            
        arr = []
        
        helper(root)
        
        return collaborator(arr)
