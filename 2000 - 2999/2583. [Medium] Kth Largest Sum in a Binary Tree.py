# https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        def helper(node, lvl):
            if node: 
                counter[lvl] += node.val
                
                helper(node.left, lvl + 1)
                helper(node.right, lvl + 1)
        
        counter = defaultdict(lambda: 0)
        
        helper(root, 0)
        
        arr = [counter[key] for key in counter]
        
        if k > len(arr):
            return -1 
        
        else: 
            arr.sort(key = lambda item: -item) 
            
            return arr[k - 1]
        
