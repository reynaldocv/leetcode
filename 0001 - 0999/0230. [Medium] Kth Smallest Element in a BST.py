# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(node):
            nonlocal ans, counter
            
            if node: 
                helper(node.left)
                
                counter += 1 
                
                if counter == k: 
                    ans = node.val
                
                helper(node.right)
                
        ans = 0 
        
        counter = 0 
        
        helper(root)
        
        return ans 
