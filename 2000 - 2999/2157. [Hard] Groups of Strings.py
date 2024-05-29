# https://leetcode.com/problems/groups-of-strings/

# https://leetcode.com/problems/groups-of-strings/

class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        def helper(u):
            while u != parent[u]:
                u = parent[u]
            
            return u
        
        def collaborator(u, v):
            parentU = helper(u)
            parentV = helper(v)
            
            parent[parentU] = parent[parentV] = min(parentU, parentV)
            
        n = len(words)
        
        parent = [i for i in range(n)]
        
        seen = {}
        
        values = {chr(ord("a") + i): i for i in range(26)}
        
        for (i, word) in enumerate(words):   
            mask = sum([1 << values[char] for char in word])
            
            if mask in seen: 
                collaborator(i, seen[mask])
                
            for k in range(26): 
                if mask ^ (1 << k) in seen: 
                    collaborator(i, seen[mask ^ (1 << k)])
                    
                if mask & (1 << k): 
                    newMask = mask ^ (1 << k) ^ (1 << 26)
                    if newMask in seen: 
                        collaborator(i, seen[newMask])
                    
                    seen[newMask] = i
                    
            seen[mask] = i 
            
        counter = defaultdict(lambda: 0)
        
        maxElems = 0 
        
        for i in range(n):
            counter[helper(i)] += 1 
            
            maxElems = max(maxElems, counter[helper(i)])
            
        return (len(counter), maxElems)
        
        
