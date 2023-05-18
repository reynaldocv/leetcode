# https://leetcode.com/problems/even-odd-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        def helper(node, lvl):
            if node: 
                if lvl % 2 == 0:    
                    if node.val % 2 == 0 or even[lvl] >= node.val:
                        return False 
                    
                    even[lvl] = node.val
                    
                else: 
                    if node.val % 2 == 1 or odd[lvl] <= node.val:
                        return False 
                    
                    odd[lvl] = node.val
                    
                return helper(node.left, lvl + 1) and helper(node.right, lvl + 1)
            
            else: 
                return True 
                
        even = defaultdict(lambda: -inf)
        odd = defaultdict(lambda: inf)
        
        return helper(root, 0)
  
