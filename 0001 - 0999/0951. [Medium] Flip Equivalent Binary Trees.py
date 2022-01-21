# https://leetcode.com/problems/flip-equivalent-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def helper(node1, node2):            
            if node1 and node2: 
                if node1.val == node2.val: 
                    if helper(node1.left, node2.left) and helper(node1.right, node2.right):
                        return True
                    return helper(node1.left, node2.right) and helper(node1.right, node2.left)
                    
                else: 
                    return False
                
            elif not node1 and not node2: 
                return True
            else: 
                return False
        
        return helper(root1, root2)
                
            

            
        
