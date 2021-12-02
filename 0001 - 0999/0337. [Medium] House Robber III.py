# https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache 
        def helper(root, val):
            if root: 
                if val == True: 
                    aux1 = root.val + helper(root.left, False) + helper(root.right, False)
                    aux2 = helper(root.left, True) + helper(root.right, True)
                    
                    return max(aux1, aux2)
                    
                else: 
                    return helper(root.left, True) + helper(root.right, True)
            
            else: 
                return 0
            
        return max(helper(root, True), helper(root, False))
                
