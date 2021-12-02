# https://leetcode.com/problems/unique-binary-search-trees-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate(start, end, exists):
            key = str(start) + str(end)
            if key not in exists: 
                if start > end: 
                    exists[key] = [None]
                else: 
                    ans = []
                    for i in range(start, end + 1):
                        leftTrees = generate(start, i - 1, exists)
                        rightTrees = generate(i + 1, end, exists)
                        for left in leftTrees: 
                            for right in rightTrees: 
                                root = TreeNode(i)
                                root.left = left
                                root.right = right
                                ans.append(root)
                    exists[key] = ans
            return exists[key]
        
        exists = {}
        return generate(1, n, exists)
        
                
            
