# https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2: 
            return [i for i in range(n)]
        
        neighbors = [set() for i in range(n)]
        
        for (u, v) in edges: 
            neighbors[u].add(v)
            neighbors[v].add(u)
        
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1: 
                leaves.append(i)
        
        remaining_nodes = n
        
        while remaining_nodes > 2: 
            remaining_nodes -= len(leaves)
            
            newLeaves = []
            
            while leaves: 
                leaf = leaves.pop()
                neighbor = neighbors[leaf].pop()
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1: 
                    newLeaves.append(neighbor)
                    
            leaves = newLeaves
            
        return leaves
        
