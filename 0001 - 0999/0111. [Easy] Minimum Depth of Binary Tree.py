# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def helper(node, lvl):
            if node: 
                if not node.left and not node.right: 
                    return lvl + 1
                
                left = helper(node.left, lvl + 1)
                right = helper(node.right, lvl + 1)
                
                return min(left, right)
            
            else: 
                return inf
            
        ans = helper(root, 0)
        
        return 0 if ans == inf else ans 
