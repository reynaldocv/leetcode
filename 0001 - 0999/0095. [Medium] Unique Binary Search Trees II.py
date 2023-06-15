# https://leetcode.com/problems/unique-binary-search-trees-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @cache 
        def helper(start, end):
            if start == end:
                return [TreeNode(start)]
            
            elif end > start: 
                ans = []
                
                for num in range(start, end + 1):
                    for left in helper(start, num - 1): 
                        for right in helper(num + 1, end):
                            node = TreeNode(num)
                            
                            node.left = left
                            node.right = right 
                            
                            ans.append(node)
                            
                return ans 
            
            else: 
                return [None]
            
        return helper(1, n)
        
                
            
