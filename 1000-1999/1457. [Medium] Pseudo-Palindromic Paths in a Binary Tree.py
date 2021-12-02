# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def isPalindromic():                        
            odd = 0
            for key in seen: 
                if seen[key] % 2 == 1: 
                    odd += 1
                    if odd > 1:
                        return False            
            return True
        
        def helper(root):
            if root: 
                seen[root.val] += 1
                if not root.left and not root.right:
                    if isPalindromic():
                        self.ans += 1
                helper(root.left)
                helper(root.right)
                seen[root.val] -= 1
            
        seen = defaultdict(int)
        self.ans = 0
        helper(root)
        
        return self.ans
