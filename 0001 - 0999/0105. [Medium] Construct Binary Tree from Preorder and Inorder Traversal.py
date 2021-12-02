# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def createTree(preorder, inorder):
            if len(preorder) == 0: 
                return None
            else: 
                elem = preorder[0]
                root = TreeNode(elem)
                idx = inorder.index(elem)
                root.left = createTree(preorder[1: idx + 1], inorder[:idx])
                root.right = createTree(preorder[idx + 1:], inorder[idx + 1:])
                return root
            
        ans = createTree(preorder, inorder)
        return ans
        
