# https://leetcode.com/problems/find-mode-in-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        
        def counter(root):
            if root: 
                self.dic[root.val] = self.dic.get(root.val, 0) + 1
                counter(root.left)
                counter(root.right)
            
        dic = self.dic = {}
        counter(root)
        aux = []
        for i in dic: 
            aux.append((dic[i], i))
        aux.sort(reverse = True)
        max_ = aux[0][0]         
        ans = [aux[0][1]]
        for i in range(1, len(aux)):
            if aux[i][0] == max_:
                ans.append(aux[i][1])
            else:
                break 
        return ans
            
