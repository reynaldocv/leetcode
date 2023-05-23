# https://leetcode.com/problems/path-sum-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def helper(node, arr):
            if node: 
                arr.append(node.val)
            
                if not node.left and not node.right: 
                    
                    if sum(arr) == targetSum: 
                        ans.append(arr[: ])
                
                helper(node.left, arr)
                helper(node.right, arr)
                
                arr.pop() 
        
        ans = []
        
        helper(root, [])
        
        return ans 
        
                    
        
        
