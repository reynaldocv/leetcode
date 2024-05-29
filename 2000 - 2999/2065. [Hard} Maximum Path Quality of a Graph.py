# https://leetcode.com/problems/maximum-path-quality-of-a-graph/

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        n = len(values)
        
        values = {ith: val for (ith, val) in enumerate(values)}
        
        graph = [[] for _ in range(n)]
        
        for (u, v, time) in edges: 
            graph[u].append((v, time))
            graph[v].append((u, time))
            
        stack = [(0, 0, values[0], 1)]
        
        ans = 0 
        
        while stack: 
            (u, totalTime, totalValue, mask) = stack.pop() 
            
            if u == 0: 
                ans = max(ans, totalValue)
            
            for (v, time) in graph[u]:
                if totalTime + time <= maxTime: 
                    if mask & (1 << v): 
                        stack.append((v, totalTime + time, totalValue, mask))
                        
                    else: 
                        stack.append((v, totalTime + time, totalValue + values[v], mask ^ (1 << v)))
                        
        return ans                
                        
                                     
