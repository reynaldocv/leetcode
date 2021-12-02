# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def helper(root, lvl):
            if root: 
                seen[lvl] += root.val
                helper(root.left, lvl + 1)
                helper(root.right, lvl + 1)
                
        seen = defaultdict(lambda: 0)
        
        helper(root, 1)
        
        ans = (-inf, 0)
        
        for key in seen: 
            if ans[0] == seen[key]:
                ans = (ans[0], min(ans[1], key))
            else: 
                ans = max(ans, (seen[key], key))
            
        return ans[1]
        
