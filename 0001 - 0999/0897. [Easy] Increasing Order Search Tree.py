# https://leetcode.com/problems/increasing-order-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def helper(node):
            if node:                 
                return helper(node.left) + [node] + helper(node.right)                
                
            else: 
                return []
            
        arr = helper(root)
        
        n = len(arr)
        
        for i in range(n - 1):
            arr[i].left = None
            arr[i].right = arr[i + 1]
            
        arr[-1].left = None 
        arr[-1].right = None 
        
        return arr[0]

class Solution2:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def helper(node):
            nonlocal cur 
            
            if node:          
                helper(node.left)
                
                cur.right = TreeNode(node.val)                
                cur = cur.right
                
                helper(node.right)
                
        ans = cur = TreeNode(0)
        
        helper(root)
        
        return ans.right
