# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def helper(node, lvl):
            nonlocal ans 
            
            if node: 
                if lvl - 2 in seen: 
                    ans += node.val
                    
                if node.val % 2 == 0: 
                    seen.add(lvl)

                helper(node.left, lvl + 1)
                helper(node.right, lvl + 1)
                    
                if node.val % 2 == 0:
                    seen.remove(lvl)
            
        ans = 0 
        
        seen = set()
        
        helper(root, 0)
        
        return ans 
