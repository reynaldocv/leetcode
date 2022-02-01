# https://leetcode.com/problems/groups-of-strings/

class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        def helper(node):
            while node != parent[node]:
                node = parent[node]
            
            return node
        
        def collaborator(node1, node2):
            parent1, parent2 = helper(node1), helper(node2)
            parent[parent1] = parent[parent2] = min(parent1, parent2)
            
        n = len(words)
        
        parent = [i for i in range(n)]
        
        seen = {}
        values = {chr(ord("a") + i): i for i in range(26)}
        
        for (i, word) in enumerate(words):   
            m = sum([1 << values[char] for char in word])
            if m in seen: 
                collaborator(i, seen[m])
                
            for k in range(26): 
                if m ^ (1 << k) in seen: 
                    collaborator(i, seen[m ^ 1 << k])
                    
                if m & (1 << k): 
                    mm = m ^ (1 << k) ^ (1 << 26)
                    if mm in seen: 
                        collaborator(i, seen[mm])
                    
                    seen[mm] = i
                    
            seen[m] = i 
            
        counter = defaultdict(lambda: 0)
        for i in range(n):
            counter[helper(i)] += 1 
            
        return [len(counter), max(counter.values())]
