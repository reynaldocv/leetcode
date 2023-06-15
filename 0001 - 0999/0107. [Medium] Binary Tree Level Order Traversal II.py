# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(node, lvl):
            if node: 
                helper(node.left, lvl + 1)
                
                seen[lvl].append(node.val)
                
                helper(node.right, lvl + 1)
                
        seen = defaultdict(lambda: [])
        
        helper(root, 0)
        
        n = len(seen)
        
        return [seen[i] for i in range(n)][:: -1]
        
