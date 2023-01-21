# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def helper(node, val):
            if node: 
                if node.val == val: 
                    return node
                
                elif val < node.val: 
                    return helper(node.left, val)
                
                else: 
                    return helper(node.right, val)
                
            return None
        
        return helper(root, val)
                
        
