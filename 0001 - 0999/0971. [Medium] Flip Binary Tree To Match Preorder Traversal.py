# https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        def helper(node):
            nonlocal i, flipped
            if node: 
                if node.val != voyage[i]:
                    flipped = [-1]
                    
                else: 
                    i += 1 

                    if (i < len(voyage) and node.left and node.left.val != voyage[i]):
                        flipped.append(node.val)
                        helper(node.right)
                        helper(node.left)
                    else: 
                        helper(node.left)
                        helper(node.right)

        flipped = []
        i = 0 
        
        helper(root)
        
        if flipped and flipped[0] == -1: 
            flipped = [-1]
            
        return flipped
           
                    
        
