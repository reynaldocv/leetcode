# https://leetcode.com/problems/binary-tree-paths/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def helper(node, path):
            if node: 
                if path == "":
                    path += str(node.val)
                else: 
                    path += "->" + str(node.val)
                    
                if not node.left and not node.right: 
                    ans.append(path)
                    
                helper(node.left, path)
                helper(node.right, path)
                
        ans = []
        
        helper(root, "")
        
        return ans 
