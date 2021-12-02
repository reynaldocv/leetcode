# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root):
            if not root: 
                return Result(None, 0)
            else: 
                L = helper(root.left)
                R = helper(root.right)
                if L.dist > R.dist: 
                    return Result(L.node, L.dist + 1)
                elif L.dist < R.dist:
                    return Result(R.node, R.dist + 1)
                else: 
                    return Result(root, L.dist + 1)
        
        Result = namedtuple("Result", ("node", "dist"))
        return helper(root).node
       
