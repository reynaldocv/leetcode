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
                leftSum, leftQnt = helper(node.left)
                rightSum, rightQnt = helper(node.right)
                
                aSum = leftSum + rightSum + node.val
                qnt = leftQnt + rightQnt + 1
                
                if aSum//qnt == node.val: 
                    ans += 1 
                
                return aSum, qnt
                
            else: 
                return 0, 0
            
        ans = 0 
        
        helper(root)
        
        return ans 
        
