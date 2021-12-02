# https://leetcode.com/problems/most-frequent-subtree-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root):
            nonlocal m
            if root: 
                left = helper(root.left)
                right = helper(root.right)
                val = root.val + left + right
                counter[val] += 1
                m = max(m, counter[val])
                return val
            else: 
                return 0
            
        counter = defaultdict(lambda: 0)        
        m = 0
        helper(root)
        
        ans = []
        
        for key in counter: 
            if counter[key] == m: 
                ans.append(key)
                
        return ans
        
