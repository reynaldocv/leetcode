# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def helper(node, arr):
            if node:
                helper(node.left, arr)
                
                arr.append(node.val)
                
                helper(node.right, arr)
                
        arr1 = []
        arr2 = []
        
        helper(root1, arr1)
        helper(root2, arr2)
        
        m, n = len(arr1), len(arr2)
        i, j = 0, 0
        
        ans = []
        
        while i < m or j < n: 
            val1 = arr1[i] if i < m else inf 
            val2 = arr2[j] if j < n else inf 
            
            if val1 < val2: 
                ans.append(val1)
                
                i += 1 
                
            else: 
                ans.append(val2)
                
                j += 1 
                
        return ans 
                
            
        
            
        
        
