# https://leetcode.com/problems/number-of-operations-to-make-network-connected/

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def assignGroup(i, elem):
            visited = {i: True}
            stack = [i]
            groups[i] = elem
            while stack: 
                u = stack.pop()
                for v in graph[u]:
                    if v not in visited: 
                        groups[v] = elem
                        stack.append(v)
                        visited[v] = True
                
        graph = [[] for _ in range(n)]
        degree = [0 for _ in range(n)]
        
        for (u, v) in connections: 
            degree[u], degree[v] = degree[u] + 1, degree[v] + 1
            graph[u].append(v)            
            graph[v].append(u)
            
        groups = [-1 for _ in range(n)]
        
        elem = -1
        for i in range(n):
            if groups[i] == -1: 
                elem += 1                
                assignGroup(i, elem)
                
        vertices = defaultdict(lambda: 0)
        degrees = defaultdict(lambda: 0)
        
        for i in range(n): 
            vertices[groups[i]] += 1
            degrees[groups[i]] += degree[i]
       
        rest = 0 
        for key in degrees: 
            if degrees[key] != 0:
                rest += degrees[key]//2 - vertices[key] + 1
        
        return elem if rest >= elem else -1
            
