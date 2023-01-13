# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def helper(node, minimum):
            if node: 
                ans = inf 
                
                if node.val != minimum: 
                    ans = min(ans, node.val)
                    
                left = helper(node.left, minimum)
                
                if left != minimum: 
                    ans = min(ans, left)
                    
                right = helper(node.right, minimum)
                
                if right != minimum: 
                    ans = min(ans, right)
                    
                return ans 
                    
            return inf     
        
        minimum = inf 
        
        minimum = helper(root, minimum)
        
        ans = helper(root, minimum)
        
        return -1 if ans == inf else ans
                
        
                
