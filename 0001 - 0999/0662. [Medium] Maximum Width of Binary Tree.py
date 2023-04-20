# https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(position, lvl, node):
            if node: 
                minimum[lvl] = min(minimum[lvl], position)
                maximum[lvl] = max(maximum[lvl], position)
                
                helper(2*position, lvl + 1, node.left)
                helper(2*position + 1, lvl + 1, node.right)
            
        minimum = defaultdict(lambda: inf)
        maximum = defaultdict(lambda: -inf)

        helper(0, 0, root)

        ans = 0 

        for key in minimum: 
            ans = max(ans, maximum[key] - minimum[key] + 1)

        return ans
