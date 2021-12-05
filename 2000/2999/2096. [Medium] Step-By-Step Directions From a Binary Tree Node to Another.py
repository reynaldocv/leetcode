# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def firstCommonParent(root, p, q):
            if not root: 
                return None
            
            if root.val in (p, q):
                return root
            
            left = firstCommonParent(root.left, p, q)
            right = firstCommonParent(root.right, p, q)
            
            if left and right: 
                return root
            else: 
                return left if left else right
            
        def paths(root, p):
            stack = [(root, "")]
            while stack: 
                (node, path) = stack.pop()
                if node.val == p: 
                    return path
                else: 
                    if node.left: 
                        stack.append((node.left, path + "L"))
                    if node.right: 
                        stack.append((node.right, path + "R"))
        
        node = firstCommonParent(root, startValue, destValue)
        
        path1 = paths(node, startValue)
        path2 = paths(node, destValue)
        
        return "U"*len(path1) + path2
        
class Solution2:
    def getDirections(self, root: Optional[TreeNode], p: int, q: int) -> str:
        def firstCommonParent(root, p, q):
            if not root:
                return None
            if root.val in (p, q):
                return root
            
            left  = firstCommonParent(root.left, p, q)
            right = firstCommonParent(root.right, p, q)
            
            if left and right: 
                return root
            else: 
                return left if left else right
        
        def helper(root, p):
            if root: 
                if root.val == p: 
                    return "*"
                
                left = helper(root.left, p)
                right = helper(root.right, p)
                if left or right:                 
                    return "L" + left if left else "R" + right
                
            return ""
        
        node = firstCommonParent(root, p, q)
        path1 = helper(node, p)
        path2 = helper(node, q)
        
        return "U"*(len(path1) - 1) + path2[:-1]
        
