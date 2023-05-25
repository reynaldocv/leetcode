# https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def helper(node, aSum):
            nonlocal ans
            
            if node: 
                aSum += node.val 
                
                ans += counter[aSum - targetSum]                
                
                counter[aSum] += 1 
                
                helper(node.left, aSum)
                helper(node.right, aSum)
                
                counter[aSum] -= 1 
                        
        counter = defaultdict(lambda: 0)        
        counter[0] = 1
        
        ans = 0 
        
        helper(root, 0)
        
        return ans 
