# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def find(value):
            while value != parent.get(value, value):
                value = parent.get(value, value)
                
            return value
        
        def union(val1, val2):
            parent1 = find(val1)
            parent2 = find(val2)
            
            parent[parent1] = parent[parent2] = min(parent1, parent2)
            
        n = len(stones)
        parent = defaultdict(lambda: inf)
        
        for (x, y) in stones: 
            union(x, ~y)
            
        ans = n 
        seen = {}
        
        for (x, y) in stones: 
            seen[find(x)] = True 
            seen[find(~y)] = True 
            
        return ans - len(seen)  
