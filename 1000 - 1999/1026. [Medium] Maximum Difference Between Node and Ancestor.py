# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(node, minVal, maxVal):
            nonlocal ans 
            
            if node: 
                ans = max(ans, abs(minVal - node.val), abs(maxVal - node.val))
                
                minVal = min(minVal, node.val)
                maxVal = max(maxVal, node.val)
                
                helper(node.left, minVal, maxVal)
                helper(node.right, minVal, maxVal)
                
        ans = 0 
        
        helper(root, root.val, root.val)
        
        return ans 
        
        
