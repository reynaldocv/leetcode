# https://leetcode.com/problems/print-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def depth(root):
            if root: 
                left = depth(root.left)
                right = depth(root.right)
                return 1 + max(left, right)
            else: 
                return 0 
        
        def helper(root, start, end, h):
            if root: 
                idx = (start + end)//2
                ans[h][idx] = str(root.val)
                helper(root.left, start, idx - 1, h + 1)
                helper(root.right, idx + 1, end, h + 1)
            
        
        h = depth(root)
        
        ans = [["" for _ in range(2**h - 1)] for _ in range(h)]
        
        helper(root, 0, 2**h - 2, 0)
        
        return ans
        
        
