# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def helper(root):
            if root: 
                helper(root.right)
                
                root.val += self.aux
                self.aux = root.val
                
                helper(root.left)
        
        self.aux = 0
        
        helper(root)
        
        return root

class Solution2:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def helper(node):
            if node: 
                helper(node.left)
                
                arr.append(node)
                
                helper(node.right)
        
        arr = []
        
        helper(root)
        
        n = len(arr)
        
        for i in range(n - 2, -1, -1):
            arr[i].val += arr[i + 1].val 
            
        return root
        
        
