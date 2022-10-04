# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def helper(node, lvl):
            if node: 
                sumLevel[lvl] += node.val 
                counter[lvl] += 1 
                
                left = helper(node.left, lvl + 1)
                right = helper(node.right, lvl + 1)
                
                return max(left, right) + 1
                
            else: 
                return 0 
            
        sumLevel = defaultdict(lambda: 0)
        counter = defaultdict(lambda: 0)
        
        maxLvl = helper(root, 0)
        
        return [sumLevel[i]/counter[i] for i in range(maxLvl)]
        
