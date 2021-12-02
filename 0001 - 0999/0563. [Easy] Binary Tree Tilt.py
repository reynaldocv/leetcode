#https://leetcode.com/problems/binary-tree-tilt/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def tour(root):
            if root: 
                sumL = tour(root.left)
                sumR = tour(root.right)
                self.ans.append(abs(sumL - sumR))
                return sumL + sumR + root.val
            
            else:
                return 0  
        
        
        ans = self.ans = []
        tour(root)
        return sum(ans)

        
        
