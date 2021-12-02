# https://leetcode.com/problems/all-possible-full-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        def allTrees(n):
            if n in seen:
                return seen[n]
            elif n == 1: 
                seen[1] = [TreeNode(0)]
                return seen[1]
            else:
                ans = []
                for i in range(1, n, 2):
                    leftTrees = allTrees(i)
                    rightTrees = allTrees(n - i - 1)
                    for left in leftTrees: 
                        for right in rightTrees: 
                            root = TreeNode(0)
                            root.left = left
                            root.right = right
                            ans.append(root)
                seen[n] = ans
                return seen[n]
        
        seen  = {}
        if n % 2 == 0: 
            return []
        else: 
            return allTrees(n)
            
        
