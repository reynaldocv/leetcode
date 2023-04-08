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
            if node.val not in seen:                 
                clonned = Node(node.val, [])   
                seen[node.val] = clonned

                for neighbor in node.neighbors:
                    clonned.neighbors.append(helper(neighbor))
                            
            return seen[node.val]

        if not node:
            return None
        
        seen = {}
        
        return helper(node)
    
    
