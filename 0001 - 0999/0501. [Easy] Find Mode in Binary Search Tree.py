# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def helper(node):
            nonlocal mode 
            
            if node: 
                count[node.val] += 1 
                
                mode = max(mode, count[node.val])
                
                helper(node.left)
                helper(node.right)
                
        count = defaultdict(lambda: 0)
        
        mode = 0 
        
        helper(root)
        
        return [key for key in count if count[key] == mode]
