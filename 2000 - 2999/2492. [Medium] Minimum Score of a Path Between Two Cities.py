# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        def helper(son):
            while parent[son] != son: 
                son = parent[son]
                
            return son 
        
        def collaborator(son1, son2):
            parent1 = helper(son1)
            parent2 = helper(son2)
            
            parent[parent1] = parent[parent2] = min(parent1, parent2)
            
        parent = [i for i in range(n)]
        
        for (u, v, _) in roads: 
            collaborator(u - 1, v - 1) 
            
        ans = inf 
        
        for (u, v, distance) in roads: 
            if helper(u - 1) == 0: 
                ans = min(ans, distance)
            
        return ans  
    
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(lambda: {})
        
        for (u, v, distance) in roads: 
            graph[u][v] = distance 
            graph[v][u] = distance
            
        stack = [1]
        
        seen = {1}
        
        ans = inf
        
        while stack: 
            u = stack.pop() 
            
            for v in graph[u]:
                if v not in seen: 
                    seen.add(v)
                    
                    stack.append(v)
                    
                ans = min(ans, graph[u][v])
                
        return ans if n in seen else -1
