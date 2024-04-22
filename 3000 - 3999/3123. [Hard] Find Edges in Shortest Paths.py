# https://leetcode.com/problems/find-edges-in-shortest-paths/

class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        def helper(u):
            distance = [inf for _ in range(n)]
            
            distance[u] = 0 
            
            heap = [(0, u)]
            
            while heap: 
                (dist, u) = heappop(heap)
                
                if dist == distance[u]:
                    for (v, w) in graph[u]:
                        if dist + w < distance[v]:
                            distance[v] = w + dist

                            heappush(heap, (dist + w, v))

            return distance
                    
        graph = [[] for _ in range(n)]
        
        for (u, v, w) in edges: 
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        dist0 = helper(0) 
        dist1 = helper(n - 1)
        
        m = len(edges)
        
        ans = [False for _ in range(m)]
        
        for (i, (u, v, w)) in enumerate(edges): 
            if dist0[n-1] < inf:
                if (dist0[u] + w + dist1[v] == dist0[n-1] or dist0[v] + w + dist1[u] == dist0[n-1]):
                    ans[i] = True 
                    
        return ans 
