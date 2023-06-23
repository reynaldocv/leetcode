# https://leetcode.com/problems/all-possible-full-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        @cache 
        def helper(n):
            if n == 1: 
                return [TreeNode(0)]
            
            else: 
                ans = []
                for i in range(1, n, 2):                    
                    for left in helper(i):
                        for right in helper(n - 1 - i):
                            node = TreeNode(0, left, right)
                            
                            ans.append(node)
                    
                return ans 
            
        return helper(n)
        
                            
            
            
            
        
