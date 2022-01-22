# https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def helper(child):
            while child != parent[child]:
                child = parent[child]
                
            return child
        
        def collaborator(child1, child2):
            parent1 = helper(child1)
            parent2 = helper(child2)
            parent[parent1] = parent[parent2] = min(parent1 , parent2)
        
        heap = []
        n = len(points)
        for i in range(1, n):
            for j in range(i):
                manhattan = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heappush(heap, (manhattan, i, j))
                
        edges = 0 
        parent = [i for i in range(n)]
        
        ans = 0 
        
        while edges < n - 1:
            (distance, u, v) = heappop(heap)
            if helper(u) != helper(v):
                collaborator(u, v)
                ans += distance
                edges += 1 
                
        return ans
                
            
            
            
                
            
        
        
        
