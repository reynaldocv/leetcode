# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(preOrder, inOrder):
            if preOrder: 
                value = preOrder[0]
                
                idx = inOrder.index(value) 
                
                ans = TreeNode(value)
                
                ans.left = helper(preOrder[1: idx + 1], inOrder[: idx])
                ans.right = helper(preOrder[idx + 1: ], inOrder[idx + 1: ])
                
                return ans 
            
            else: 
               return None 
            
        return helper(preorder, inorder)
        
        
        
        
