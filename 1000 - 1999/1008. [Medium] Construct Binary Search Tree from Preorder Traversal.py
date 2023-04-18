# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def helper(arr):
            if arr: 
                value = arr[0]
                
                idx = bisect_left(arr, value + 1)
                
                ans = TreeNode(value)
                ans.left = helper(arr[1: idx])
                ans.right = helper(arr[idx: ])
                
                return ans 
            else: 
                return None
            
        return helper(preorder)
        
