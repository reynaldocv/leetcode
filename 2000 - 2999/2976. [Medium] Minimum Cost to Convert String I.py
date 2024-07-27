# https://leetcode.com/problems/minimum-cost-to-convert-string-i/

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        m = len(cost)
        
        distance = defaultdict(lambda: defaultdict(lambda: inf))
        
        nodes = set()
        
        for i in range(m):
            u = original[i]
            v = changed[i]
            dist = cost[i]
            
            distance[u][v] = min(distance[u][v], dist)
            
            nodes.add(u)
            nodes.add(v)
            
        for u in nodes: 
            distance[u][u] = 0
            
        for k in nodes: 
            for u in nodes: 
                for v in nodes: 
                    distance[u][v] = min(distance[u][v], distance[u][k] + distance[k][v])
                    
        n = len(source)
        
        ans = 0 
        
        for i in range(n):
            u = source[i]
            v = target[i]
            
            if distance[u][v] == inf: 
                return -1 
            
            ans += distance[u][v]
            
        return ans
                    
        
            
        
