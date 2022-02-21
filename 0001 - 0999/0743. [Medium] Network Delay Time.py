# https://leetcode.com/problems/network-delay-time/

# Bellman-Ford algorithm
# Time complexity O(VE)
# Space complexity O(V)
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distance = [inf for _ in range(n)]
        distance[k - 1] = 0 
        
        for _ in range(n - 1):
            for (u, v, time) in times: 
                distance[v - 1] = min(distance[v - 1], distance[u - 1] + time)
            
        ans = max(distance)
        
        return ans if ans < inf else -1

# Floyd-Warshall algorithm
# Time complexity O(V^3)
# Space complexity O(V^2)
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distance = [[inf for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            distance[i][i] = 0 
            
        for (u, v, time) in times: 
            distance[u - 1][v - 1] = time
            
        for mid in range(n):
            for u in range(n):
                for v in range(n):
                    distance[u][v] = min(distance[u][v], distance[u][mid] + distance[mid][v])
                    
        ans = max(distance[k - 1])
        
        return ans if ans < inf else -1 
      
# Dijkstra algorithm
# Time complexity O(E lg E)
# Space complexity O(E)       
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(lambda: [])
        for (u, v, time) in times: 
            graph[u].append((time, v))
        
        distance = [inf for _ in range(n)]
        
        heap = [(0, k)]
        
        while heap: 
            (t, u) = heappop(heap)
            if distance[u - 1] == inf: 
                distance[u - 1] = t
                for (time, v) in graph[u]:
                    heappush(heap, (t + time, v))

        ans = max(distance)
        
        return ans if ans < inf else -1 
      
# DFS
# Time complexity O(V^V + ElogE)
# Space complexity O(V)      
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(lambda: [])
        for (u, v, time) in times: 
            graph[u].append((time, v))
            
        for key in graph:
            graph[key].sort(reverse = True)
        
        distance = [inf for _ in range(n)]
        
        stack = [(0, k)]
        
        while stack: 
            (t, u) = stack.pop()
            if distance[u - 1] > t: 
                distance[u - 1] = t 
                for (time, v) in graph[u]: 
                    stack.append((t + time, v))
                    
        ans = max(distance)
        
        return ans if ans < inf else -1
      
# BFS
# Time complexity O(V^V + ElogE)
# Space complexity O(V)            
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(lambda: [])
        for (u, v, time) in times: 
            graph[u].append((time, v))
            
        for key in graph:
            graph[key].sort()
        
        distance = [inf for _ in range(n)]
        
        stack = [(0, k)]
        
        while stack: 
            (t, u) = stack.pop(0)
            if distance[u - 1] > t: 
                distance[u - 1] = t 
                for (time, v) in graph[u]: 
                    stack.append((t + time, v))
                    
        ans = max(distance)
        
        return ans if ans < inf else -1
