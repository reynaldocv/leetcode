# https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(u):
            while u != parent[u]:
                u = parent[u]
            
            return u
        
        equations.sort(key = lambda item: 1 if item.count("!=") else 0)
        
        idx = 0 
        parent = {}
        
        for elem in equations: 
            u = elem[:1]
            operation = elem[1:3]
            v = elem[3:]
            if u not in parent: 
                parent[u] = u
            if v not in parent: 
                parent[v] = v
            
            pu = find(u)
            pv = find(v)
                
            if operation == "==":
                parent[pu] = parent[pv] = min(pu, pv)
            elif pu == pv:
                return False
            
        return True
                
                
                
