# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        def high(root, h):
            if root:
                self.dic[h] = self.dic.get(h, [])
                self.dic[h].append(root.val)
                high(root.left, h + 1)
                high(root.right, h + 1)
            
        dic = self.dic = {}
        high(root, 0)
        ans = [0]*len(dic)
        for i in dic:
            ans[i] = sum(dic[i])/len(dic[i])
        return ans
        
