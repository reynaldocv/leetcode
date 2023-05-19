# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, maxElem):
            nonlocal ans 
            
            if node: 
                if node.val >= maxElem:
                    ans += 1 
                    
                maxElem = max(maxElem, node.val)
                    
                helper(node.left, maxElem)
                helper(node.right, maxElem)
        
        ans = 0 
        
        helper(root, -inf)
        
        return ans 
        
        
        
        
        
        
        
        
        
