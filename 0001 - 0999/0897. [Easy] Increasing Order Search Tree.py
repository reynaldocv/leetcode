# https://leetcode.com/problems/increasing-order-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        
        def incrBST(root):             
            if root != None:
                incrBST(root.left)                
                self.ans.right = TreeNode(root.val)
                self.ans = self.ans.right
                incrBST(root.right)
        
        ans = self.ans = TreeNode(0)
        incrBST(root)
        return ans.right
        
