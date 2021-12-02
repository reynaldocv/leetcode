# https://leetcode.com/problems/binary-tree-paths/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def route(root, ans):
            if root: 
                if root.left == None and root.right == None: 
                    self.ans.append(ans + "->" + str(root.val))
                else: 
                    route(root.left, ans + "->" + str(root.val))
                    route(root.right, ans + "->" + str(root.val))
        ans = self.ans = []
        route(root, "")
        for i in range(len(ans)):
            ans[i] = ans[i][2:]
        return ans
