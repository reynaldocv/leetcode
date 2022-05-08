# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            nonlocal ans
            if node: 
                (left, leftQ) = helper(node.left)
                (right, rightQ) = helper(node.right)
                
                if (left + right + node.val)//(leftQ + rightQ + 1) == node.val:
                    ans += 1 
                    
                return (left + right + node.val, leftQ + rightQ + 1)
                
            else:
                return (0, 0) 
            
        ans = 0 
        
        helper(root)
        
        return ans 
        
