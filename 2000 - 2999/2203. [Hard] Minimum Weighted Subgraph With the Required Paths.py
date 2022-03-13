# https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        def helper(u, graph):
            distance = [inf for _ in range(n)]
            distance[u] = 0 
            stack = [(u, 0)]
            
            while stack: 
                (u, dist) = stack.pop(0)
                if distance[u] == dist: 
                    for (v, edge) in graph[u]:
                        if dist + edge < distance[v]:
                            distance[v] = dist + edge
                            stack.append((v, dist + edge))
            return distance 
        
        graph = [[] for _ in range(n)]
        trans = [[] for _ in range(n)]
        for (u, v, edge) in edges: 
            graph[u].append((v, edge))
            trans[v].append((u, edge))
        
        distance1 = helper(src1, graph)
        distance2 = helper(src2, graph)
        distance3 = helper(dest, trans)
        
        ans = inf
        for i in range(n):
            ans = min(ans, distance1[i] + distance2[i] + distance3[i])
            
        return ans if ans < inf else -1 
