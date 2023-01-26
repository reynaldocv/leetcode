# https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(lambda: {})
        
        for (a, b, price) in flights: 
            graph[a][b] = price
            
        distance = defaultdict(lambda: inf)
        
        distance[src] = 0
            
        stack = [(src, 0, 0)]
        
        while stack: 
            (u, dist, steps) = stack.pop(0) 
            
            if steps <= k:             
                for v in graph[u]:
                    newDistance = dist + graph[u][v]
                    if distance[v] > newDistance:
                        distance[v] = newDistance
                        
                        stack.append((v, newDistance, steps + 1))
                        
        return -1 if distance[dst] == inf else distance[dst]
        
        
        
        
