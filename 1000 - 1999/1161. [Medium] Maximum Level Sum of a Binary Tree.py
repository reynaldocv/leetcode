# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def helper(node, lvl):
            if node: 
                aSum[lvl] += node.val 
                
                helper(node.left, lvl + 1)
                helper(node.right, lvl + 1)
        
        aSum = defaultdict(lambda: 0)
        
        ans = (-inf, -1)
        
        helper(root, 1)
        
        for key in aSum: 
            ans = max(ans, (aSum[key], -key))
            
        return -ans[1]
        
        
