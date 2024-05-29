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
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def helper(node):
            if node: 
                if node.val == startValue or node.val == destValue: 
                    return node
                
                else: 
                    left = helper(node.left)
                    right = helper(node.right)
                    
                    if left and right: 
                        return node 
                    
                    elif left: 
                        return left 
                    
                    else: 
                        return right 
                    
            else: 
                return None 
            
        def collaborator(node, value):
            if node: 
                if node.val == value: 
                    return "*"
                
                else: 
                    left = collaborator(node.left, value)
                    right = collaborator(node.right, value)
                    
                    if left or right:
                        if left: 
                            return "L" + left
                    
                        else: 
                            return "R" + right
                        
                    else: 
                        return ""
                    
            else: 
                return ""                    
        
        parent = helper(root)
        
        prefix = collaborator(parent, startValue)[: -1]        
        prefix = "U"*len(prefix)
        
        suffix = collaborator(parent, destValue)[: -1]
        
        return prefix + suffix
            
        
