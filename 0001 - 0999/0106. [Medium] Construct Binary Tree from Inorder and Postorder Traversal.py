# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(inArr, postArr):
            if inArr: 
                value = postArr[-1]  
                
                idx = inArr.index(value)
                
                ans = TreeNode(value)
                
                ans.left = helper(inArr[: idx], postArr[: idx])
                ans.right = helper(inArr[idx + 1: ], postArr[idx : -1])
                
                return ans 
            
            return None 
        
        return helper(inorder, postorder)
