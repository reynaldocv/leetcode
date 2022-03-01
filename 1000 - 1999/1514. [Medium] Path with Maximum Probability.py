# https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(lambda: [])
        for (i, (u, v)) in enumerate(edges): 
            graph[u].append((succProb[i], v))
            graph[v].append((succProb[i], u))
            
        probability = defaultdict(lambda: 0)
        probability[start] = 1
        
        heap = [(-1, start)]
        ans = 0 
        while heap:             
            (preProb, u) = heappop(heap)
            if u == end:                 
                return probability[u]
                
            for (prob, v) in graph[u]:
                if -preProb*prob > probability[v]:   
                    probability[v] = -preProb*prob
                    heappush(heap, (preProb*prob, v))
            
        return 0
