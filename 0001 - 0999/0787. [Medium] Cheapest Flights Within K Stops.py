# https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(lambda: [])
        for (u, v, price) in flights:
            graph[u].append((v, price))
            
        prices = defaultdict(lambda: inf)
        prices[src] = 0
        
        stack = [(0, 0, src)]
        
        while stack:
            (price, flies, u) = stack.pop(0)
            if flies <= k: 
                for (v, p) in graph[u]:
                    if prices[v] > price + p:
                        prices[v] = price + p
                        stack.append((prices[v], flies + 1, v))
                    
        return -1 if prices[dst] == inf else prices[dst]
        
        
        
        
