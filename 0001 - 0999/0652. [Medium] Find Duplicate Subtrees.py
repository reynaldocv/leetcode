# https://leetcode.com/problems/find-duplicate-subtrees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def helper(node):
            if node:
                left = helper(node.left)
                right = helper(node.right)
                ans = (node.val,) + left + right 
                counter[ans] += 1 
                nodes[ans] = node
                
            else: 
                ans = (None,)
                
            return ans 
        
        counter = defaultdict(lambda: 0)
        nodes = {}
        
        helper(root)
        
        ans = []
        for key in counter: 
            if counter[key] > 1:
                ans.append(nodes[key])
                
        return ans
        
        
        
