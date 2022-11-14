# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def helper(son):
            while son != parent[son]:
                son = parent[son]
                
            return son 
        
        n = len(stones)
        
        elems = set()
        
        for (x, y) in stones: 
            elems.add(x)
            elems.add(~y)
            
        parent = {elem: elem for elem in elems}
        
        for (x, y) in stones: 
            parentX = helper(x)
            parentY = helper(~y)
            
            parent[parentX] = parent[parentY] = min(parentX, parentY)
            
        seen = set()
        
        for key in parent:
            seen.add(helper(key))
            
        return n - len(seen)
