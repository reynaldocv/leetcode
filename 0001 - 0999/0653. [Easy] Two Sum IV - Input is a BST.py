# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def tour(root):
            if root:                
                self.dic[root.val] = self.dic.get(root.val, 0) + 1
                tour(root.left)
                tour(root.right)
        
        dic = self.dic = {}
        tour(root)
       
        for A in dic: 
            B = k - A
            if A == B and dic[A] >= 2:
                return True
            elif A != B and B in dic: 
                return True
            
        return False
           
class Solution2:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def helper(node):
            if node: 
                if k - node.val in seen: 
                    return True 
                
                seen.add(node.val)
                
                return helper(node.left) or helper(node.right)
                
            return False 
                    
        seen = set()
        
        return helper(root)
        
