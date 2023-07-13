# https://leetcode.com/problems/binary-tree-pruning/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if node: 
                leftSum, left = helper(node.left)
                rightSum, right = helper(node.right)
                
                if leftSum + rightSum + node.val == 0: 
                    return (0, None)
                
                else: 
                    return (leftSum + rightSum + node.val, TreeNode(node.val, left, right))
                
            else: 
                return (0, None)
            
        return helper(root)[1]
            
            
       
        
                    
                    
