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
                if parent != None: 
                    graph[parent].append(node.val)
                    graph[node.val].append(parent)
                    
                helper(node.val, node.left)
                helper(node.val, node.right)
                    
        graph = defaultdict(lambda: [])
        
        helper(None, root)
        
        stack = [start]
        seen = {start}
        
        ans = -1
        
        while stack: 
            newStack = []
            
            for x in stack: 
                for y in graph[x]:
                    if y not in seen: 
                        newStack.append(y)
                        
                        seen.add(y)
                     
            stack = newStack
            ans += 1 
            
        return ans  
            
        
