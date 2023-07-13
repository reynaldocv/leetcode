# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        def helper(node, lvl): 
            if node: 
                maxElem[lvl] = max(maxElem[lvl], node.val)
                
                helper(node.left, lvl + 1)
                helper(node.right, lvl + 1)
                
        maxElem = defaultdict(lambda: -inf)
        
        helper(root, 0)
        
        maxLvl = len(maxElem)
        
        return [maxElem[i] for i in range(maxLvl)]
        
        
