# https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/

class Solution:
    def canReachCorner(self, X: int, Y: int, circles: List[List[int]]) -> bool:
        def helper(u):
            while parent[u] != u:
                u = parent[u]
                
            return u 
        
        def collaboratorHorizontal(x1, y1, r, y0):
            diff = (y1 - y0)
            
            return r**2 >= diff**2
        
        def collaboratorVertical(x1, y1, r, x0):
            diff = (x1 - x0)
            
            return r**2 >= diff**2
                    
        n = len(circles)
        
        parent = [i for i in range(n)]
        
        for i in range(n):
            for j in range(n):
                (x0, y0, r0) = circles[i]
                (x1, y1, r1) = circles[j]
                
                if (x0 - x1)**2 + (y0 - y1)**2 <= (r0 + r1)**2:
                    parent0 = helper(i)
                    parent1 = helper(j)
                    
                    parent[parent0] = parent[parent1] = min(parent0, parent1)
        
        colide = defaultdict(lambda: [False for _ in range(4)])
        
        for i in range(n):
            (x0, y0, r) = circles[i]
            
            ith = helper(i)
            
            if collaboratorHorizontal(x0, y0, r, 0):
                colide[ith][2] = True 
                
            if collaboratorHorizontal(x0, y0, r, Y):
                colide[ith][1] = True 
            
            if collaboratorVertical(x0, y0, r, 0):
                colide[ith][0] = True 
                
            if collaboratorVertical(x0, y0, r, X):
                colide[ith][3] = True 

        for key in colide: 
            if any(colide[key][: 2]) and any(colide[key][2: ]) == True: 
                return False  
            
            
            
        return True
            
            
            
        
        
        
                    
        
