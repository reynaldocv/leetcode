# https://leetcode.com/problems/path-sum-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def paths(root, arr, targetSum):
            if root:
                arr.append(root.val)
                if root.left == None and root.right == None:                     
                    if sum(arr) == targetSum: 
                        self.ans.append(arr.copy())
                else: 
                    paths(root.left, arr, targetSum)
                    paths(root.right, arr, targetSum)
                arr.pop()
        
        self.ans = []
        paths(root, [], targetSum)
        
        return self.ans
                    
        
        
