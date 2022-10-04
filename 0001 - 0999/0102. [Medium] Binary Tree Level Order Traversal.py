# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(node, lvl):
            if node: 
                left = helper(node.left, lvl + 1)
                
                nodes[lvl].append(node.val)
                
                right = helper(node.right, lvl + 1)
                
                return max(left, right) + 1
                
            else: 
                return 0 
        
        nodes = defaultdict(lambda: [])
        
        maxLevel = helper(root, 0)
        
        return [nodes[i] for i in range(maxLevel)]
        
        

