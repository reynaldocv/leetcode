# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(root, lvl, idx):
            if root: 
                self.arr[idx].append((lvl, root.val))
                helper(root.left, lvl + 1, idx - 1)
                helper(root.right, lvl + 1, idx + 1)
                
        self.arr = defaultdict(lambda:[])
        helper(root, 0, 0)
        
        ans = []
        if self.arr:
            for i in range(min(self.arr), max(self.arr) + 1):
                sort = sorted(self.arr[i])
                aux = []
                for (idx, val) in sort: 
                    aux.append(val)

                ans.append(aux)

        return ans
                
        
