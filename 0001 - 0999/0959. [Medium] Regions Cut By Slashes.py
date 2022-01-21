# https://leetcode.com/problems/regions-cut-by-slashes/

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def helper(node):
            while node != parent[node]:
                node = parent[node]
                
            return node
        
        def collaborator(node1, node2):
            parent1 = helper(node1)
            parent2 = helper(node2)
            parent[parent1] = parent[parent2] = min(parent1, parent2)
        
        n = len(grid)
        parent = [i for i in range(4*n**2)]
        
        for (r, row) in enumerate(grid):
            for (c, val) in enumerate(row):
                root = 4*(r*n + c)
                if val in "/ ":
                    collaborator(root + 0, root + 1)
                    collaborator(root + 2, root + 3)                    
                if val in "\ ":
                    collaborator(root + 0, root + 2)
                    collaborator(root + 1, root + 3)
                    
                if r + 1 < n: 
                    collaborator(root + 3, (root + 4*n) + 0)
                if r - 1 >= 0: 
                    collaborator(root + 0, (root - 4*n) + 3)
                if c + 1 < n: 
                    collaborator(root + 2, (root + 4) + 1)
                if c - 1 >= 0: 
                    collaborator(root + 1, (root - 4) + 2)
                    
        ans = 0 
        for i in range(4*n**2):
            if i == helper(i):
                ans += 1 
                
        return ans
                    
                    
                
                
                    
                    
                
                
                    
                
        
        
