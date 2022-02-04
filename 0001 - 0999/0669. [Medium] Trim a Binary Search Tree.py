# https://leetcode.com/problems/trim-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def helper(node):
            if node: 
                if low <= node.val <= high:
                    node.left = helper(node.left)
                    node.right = helper(node.right)
                elif node.val < low: 
                    node = helper(node.right)
                elif node.val > high:
                    node = helper(node.left)
                    
            return node
                        
        return helper(root)
