# https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def helper(parent, node):
            if node: 
                if parent: 
                    graph[parent.val].append(node.val)
                    graph[node.val].append(parent.val)
                    
                helper(node, node.left)
                helper(node, node.right)
            
        graph = defaultdict(lambda: [])
        
        helper(None, root)
        
        stack = {start}
        seen = {start}
        
        ans = -1
        
        while stack: 
            newStack = []
            for u in stack: 
                for v in graph[u]:
                    if v not in seen: 
                        seen.add(v)
                        newStack.append(v)
                   
            stack = newStack
            ans += 1 
            
        return ans 
                        
            
        
