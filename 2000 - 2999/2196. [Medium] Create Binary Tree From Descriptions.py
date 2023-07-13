# https://leetcode.com/problems/create-binary-tree-from-descriptions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        seen = {}
        counter = defaultdict(lambda: 0)
                
        for (father, son, isLeft) in descriptions: 
            counter[son] += 1 
            
            if father not in seen: 
                seen[father] = TreeNode(father)
                
            if son not in seen: 
                seen[son] = TreeNode(son)
                
            if isLeft == 1: 
                seen[father].left = seen[son]
                
            else: 
                seen[father].right = seen[son]
                
        for key in seen: 
            if counter[key] == 0: 
                return seen[key]
            
        return None 
