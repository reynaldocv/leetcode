# https://leetcode.com/problems/most-frequent-subtree-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def helper(node):
            nonlocal maxFreq
            
            if node: 
                left = helper(node.left)
                right = helper(node.right)
                
                aSum = left + right + node.val
                
                counter[aSum] += 1 
                
                maxFreq = max(maxFreq, counter[aSum])
                
                return aSum
                
            else: 
                return 0
        maxFreq = 0 
        
        counter = defaultdict(lambda: 0)
        
        helper(root)
        
        return [key for key in counter if counter[key] == maxFreq]
        
        
