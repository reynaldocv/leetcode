# https://leetcode.com/problems/leaf-similar-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        def leafs(root):
            if root:
                if root.left == None and root.right == None: 
                    self.ans.append(root.val)
                else:
                    leafs(root.left)
                    leafs(root.right)
        
        ans1 = self.ans = []
        leafs(root1)        
        ans2 = self.ans = []
        leafs(root2)
        
        if len(ans1) == len(ans2):
            for i in range(len(ans1)):
                if ans1[i] != ans2[i]:
                    return False
            return True
        else:
            return False
