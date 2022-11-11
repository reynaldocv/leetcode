# https://leetcode.com/problems/destination-city/

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        nextCity = defaultdict(lambda: -1)
        
        for (a, b) in paths: 
            nextCity[a] = b
            
        u = paths[0][0]
        
        while nextCity[u] != -1: 
            u = nextCity[u]
            
        return u 
        
        
