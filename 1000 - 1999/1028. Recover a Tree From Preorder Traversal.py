# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        lvl = 0
        num = 0 
        arr = []
        
        for char in traversal + "-": 
            if char.isdigit():
                num = num*10 + int(char)
                
            elif char == "-":
                if num != 0: 
                    arr.append((lvl, num))
                    lvl = 0
                num = 0 
                lvl += 1
                
        (_, elem) = arr.pop(0)
        
        ans = TreeNode(elem)
        stack = [(0, ans)]
        
        for (lvl, num) in arr:
            while stack[-1][0] >= lvl: 
                stack.pop()
            
            if stack[-1][1].left: 
                stack[-1][1].right = TreeNode(num)
                stack.append((lvl, stack[-1][1].right))
            else: 
                stack[-1][1].left = TreeNode(num)
                stack.append((lvl, stack[-1][1].left))
                
        return ans
            
                
