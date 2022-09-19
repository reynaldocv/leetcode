# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node, lvl):
            if node: 
                if lvl % 2 == 1: 
                    levels[lvl].append(node)
                    
                helper(node.left, lvl + 1)
                helper(node.right, lvl + 1)

        levels = defaultdict(lambda: [])
        
        helper(root, 0)
        
        for key in levels:
            n = len(levels[key])
            for i in range(n//2):
                tmp = levels[key][i].val
                levels[key][i].val = levels[key][n - i - 1].val
                levels[key][n - i - 1].val = tmp              
                
        return root
                
