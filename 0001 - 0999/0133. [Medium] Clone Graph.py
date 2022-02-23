# https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def helper(node):
            if node.val in ans:
                return ans[node.val]
            
            clonedNode = Node(node.val, [])            
            ans[node.val] = clonedNode
            
            for neighbor in node.neighbors:
                clonedNode.neighbors.append(helper(neighbor))
            
            return clonedNode
            
        if not node:
            return None
        
        ans = {}
        helper(node)
        
        return ans[node.val]
    
    
