# https://leetcode.com/problems/maximum-path-quality-of-a-graph/

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        n = len(values)
        
        graph = [[] for _ in range(n)]
        
        for (u, v, t) in edges:
            graph[u].append((v, t))
            graph[v].append((u, t))
            
        stack = [(0, 0, values[0], 1)]
        
        ans = 0 
        
        while stack: 
            (u, time, val, mask) = stack.pop()
            
            if u == 0: 
                ans = max(ans, val)
                
            for (v, t) in graph[u]:
                if time + t <= maxTime: 
                    if not mask & (1 << v): 
                        stack.append((v, time + t, val + values[v], mask ^ 1 << v))
                        
                    else: 
                        stack.append((v, time + t, val, mask))
                        
        return ans
        
           
            
