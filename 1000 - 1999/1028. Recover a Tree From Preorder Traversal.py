# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        def helper(lvl, value):
            node = level[lvl]
            
            if node.left: 
                node.right = TreeNode(value)
                
                level[lvl + 1] = node.right
                
            else: 
                node.left = TreeNode(value)
                
                level[lvl + 1] = node.left                
        
        cnt = 0 
        num = "" 
        
        arr = []
        
        for char in traversal + "-": 
            if char == "-":
                if num != "":
                    arr.append((cnt, int(num)))
                    
                    num = ""
                    cnt = 1 
                    
                else: 
                    cnt += 1
                
            else: 
                num += char
                
        level = {}
        
        level[0] = TreeNode(0)
        
        for (lvl, num) in arr: 
            helper(lvl, num)
            
        return level[0].left
                               
                
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
                
