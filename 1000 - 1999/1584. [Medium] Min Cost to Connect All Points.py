# https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def helper(son):
            while parent[son] != son: 
                son = parent[son]
                
            return son
        
        n = len(points)
        
        heap = []
        
        for i in range(n):
            for j in range(i + 1, n):                
                x0, y0 = points[i]
                x1, y1 = points[j]
                
                distance = abs(x0 - x1) + abs(y0 - y1)
                
                heappush(heap, (distance, i, j))
                
        parent = [i for i in range(n)]
        
        ans = 0 
        
        while heap: 
            distance, u, v = heappop(heap)
            
            parentU = helper(u)
            parentV = helper(v)
            
            if parentU != parentV: 
                ans += distance 
                
                parent[parentU] = parent[parentV] = min(parentU, parentV)
                
        return ans 
                
            
            
            
                
            
        
        
        
