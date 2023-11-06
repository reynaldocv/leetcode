# https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        def helper(u):
            while u != parent[u]:
                u = parent[u]
                
            return u 
        
        inDegree = defaultdict(lambda: 0)
        
        for (u, v) in edges: 
            inDegree[v] += 1 
            
        origin = [i for i in range(n) if inDegree[i] == 0] 
        
        if len(origin) == 1: 
            return origin[0]
        
        return -1
