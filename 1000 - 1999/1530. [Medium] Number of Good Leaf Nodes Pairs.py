# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def helper(root):
            if root: 
                if not root.left and not root.right: 
                    return [0]
                else: 
                    left = helper(root.left)
                    right = helper(root.right)
                    
                    if left and right: 
                        for elem1 in left: 
                            for elem2 in right: 
                                if elem1 + elem2 + 2 <= distance: 
                                    self.ans += 1
                    arr = [elem + 1 for elem in left]
                    arr.extend([elem + 1 for elem in right])
                    
                    return arr
                    
            else: 
                return []
            
        self.ans = 0 
        helper(root)
        
        return self.ans
        
        
        
