# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def helper(node, lvl):
            if node: 
                seen[lvl] = node.val
                
                helper(node.left, lvl + 1)
                helper(node.right, lvl + 1)
        
        seen = defaultdict(lambda: None)
        
        helper(root, 0)
        
        n = len(seen)
        
        return [seen[i] for i in range(n)]
        
        
                    
                
        
