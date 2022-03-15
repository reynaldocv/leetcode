# https://leetcode.com/problems/binary-tree-coloring-game/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        def helper(node): 
            if not node: 
                return 0             
            
            else: 
                left = helper(node.left)
                right = helper(node.right)

                if node.val == x: 
                    cnt[0] = left
                    cnt[1] = right

                return 1 + left + right

        cnt = [0, 0]
        
        helper(root)
        
        return max(max(cnt), n - 1 - sum(cnt)) > n//2
        
        
