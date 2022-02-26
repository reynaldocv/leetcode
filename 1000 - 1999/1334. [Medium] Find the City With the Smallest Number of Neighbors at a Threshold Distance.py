# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distance = [[inf for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            distance[i][i] = 0
                
        for (u, v, dist) in edges: 
            distance[u][v] = dist
            distance[v][u] = dist
            
        for k in range(n):
            for u in range(n):
                for v in range(n): 
                    distance[u][v] = min(distance[u][v], distance[u][k] + distance[k][v])
                    
        ans = (inf, 0)
        
        for i in range(n):
            number = sum(1 for dist in distance[i] if dist <= distanceThreshold)
            ans = min(ans, (number, -i))
            
        return -ans[1]
