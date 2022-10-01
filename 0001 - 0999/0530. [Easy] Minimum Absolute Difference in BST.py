# https://leetcode.com/problems/minimum-absolute-difference-in-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if node: 
                helper(node.left)
                
                arr.append(node.val)
                
                helper(node.right)
        
        arr = []
        
        helper(root)
        
        n = len(arr)
        
        ans = inf
        
        for i in range(n - 1):
            ans = min(ans, arr[i + 1] - arr[i])
            
        return ans 
        
   
                           
                   
        
