# https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node1, node2):
            if not node1: 
                return node2
            if not node2: 
                return node1 
            
            val1 = node1.val if node1 else 0 
            val2 = node2.val if node2 else 0 
            
            return TreeNode(val1 + val2, helper(node1.left, node2.left), helper(node1.right, node2.right))
            
        return helper(root1, root2)
            
        
