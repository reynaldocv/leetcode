# https://leetcode.com/problems/deepest-leaves-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def helper(node, lvl):
            if node: 
                counter[lvl] += node.val 
                
                helper(node.left, lvl + 1)
                helper(node.right, lvl + 1)
            
        counter = defaultdict(lambda: 0)
        
        helper(root, 0)
        
        n = len(counter)
        
        return counter[n - 1]
