# https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(lambda: {}) 
        
        for (i, (u, v)) in enumerate(edges): 
            graph[u][v] = succProb[i]
            graph[v][u] = succProb[i]
            
        maxProbability = [0 for _ in range(n)]
        
        heap = [(-1, start)]
        
        while heap:
            (probability, u) = heappop(heap)
            
            if u == end: 
                return -probability
            
            for v in graph[u]:
                if -probability*graph[u][v] > maxProbability[v]:
                    maxProbability[v] = -probability*graph[u][v]
                    
                    heappush(heap, (-maxProbability[v], v))
            
        return 0 
