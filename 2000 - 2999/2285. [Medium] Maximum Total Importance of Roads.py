# https://leetcode.com/problems/maximum-total-importance-of-roads/

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = defaultdict(lambda: 0)
        
        for (u, v) in roads: 
            degree[u] += 1 
            degree[v] += 1 
            
        cities = [i for i in range(n)]
        
        cities.sort(key = lambda item: degree[item])
        
        ans = 0        
        
        for (value, city) in enumerate(cities, 1):
            ans += value*degree[city]
            
        return ans 
        
        
