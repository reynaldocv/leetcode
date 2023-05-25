# https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def helper(node, value):
            if node: 
                if node.val == value: 
                    minElem = collaborator(node.right)
                    
                    if minElem != None: 
                        node.val = minElem.val 
                        node.right = helper(node.right, minElem.val)
                        
                    else: 
                        node = node.left 
                    
                else: 
                    node.left = helper(node.left, value)
                    node.right = helper(node.right, value)
                    
                return node 
            
            return None            
            
        def collaborator(node):
            while node and node.left: 
                node = node.left 
            
            return node 
        
        return helper(root, key)
