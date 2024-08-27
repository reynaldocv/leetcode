# https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(lambda: [])
        
        for (ith, (u, v)) in enumerate(edges):
            probability = succProb[ith]
            
            graph[u].append((v, probability))
            graph[v].append((u, probability))            
            
        heap = [(-1, start_node)]
        seen = {start_node}
        
        while heap: 
            (probability, u) = heappop(heap)
            
            seen.add(u)
                
            if u == end_node:
                return -probability                 
                
            for (v, prob) in graph[u]:
                if v not in seen: 
                    heappush(heap, (probability*prob, v))
                    
        return 0
