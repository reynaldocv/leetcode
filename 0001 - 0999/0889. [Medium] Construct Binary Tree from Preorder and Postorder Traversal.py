# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(preorder, postorder):
            if len(preorder) == 0: 
                return None
            elif len(preorder) == 1: 
                return TreeNode(preorder[0])
            else: 
                val = preorder.pop(0)
                postorder.pop()
                root = TreeNode(val)
              
                elem2 = postorder[-1]                
                idx1 = preorder.index(elem2)
                
                root.left = helper(preorder[:idx1], postorder[:idx1])
                root.right = helper(preorder[idx1:], postorder[idx1:])
                return root
        
        return helper(preorder, postorder)
