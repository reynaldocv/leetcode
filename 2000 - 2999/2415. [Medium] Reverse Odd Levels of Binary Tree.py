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
                helper(node.left, lvl + 1)
                
                if lvl % 2 == 1: 
                    level[lvl].append(node)
                    
                helper(node.right, lvl + 1)
                
        level = defaultdict(lambda: [])
        
        helper(root, 0)
        
        for key in level: 
            n = len(level[key])
            
            for i in range(n//2):
                level[key][i].val, level[key][n - 1 - i].val = level[key][n - 1 - i].val, level[key][i].val
                
        return root 
            
                
