# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def helper(parent, node):
            if node: 
                if parent != None: 
                    graph[node.val].append(parent)
                    graph[parent].append(node.val)
                    
                helper(node.val, node.left)
                helper(node.val, node.right)
                
        graph = defaultdict(lambda: [])
        
        helper(None, root)
    
        stack = [target.val]
        seen = {target.val}
        
        for _ in range(k):
            newStack = []
            
            for u in stack: 
                for v in graph[u]:
                    if v not in seen: 
                        seen.add(v)
                        
                        newStack.append(v)
                        
            stack = newStack
            
        return stack 
            
        
