# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def createTree(inorder, postorder):
            if len(inorder) == 0: 
                return None
            else: 
                elem = postorder[len(postorder) - 1]
                idx = inorder.index(elem)
                root = TreeNode(elem)
                root.left = createTree(inorder[:idx], postorder[:idx])
                root.right = createTree(inorder[idx + 1:], postorder[idx: -1])
                return root
        
        ans = createTree(inorder, postorder)
        return ans
