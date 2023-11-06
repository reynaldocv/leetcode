# https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/

class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        def helper(u): 
            tmp = 0 
            
            for v in graph[u]:
                if v not in visited: 
                    visited.add(v)
                    
                    tmp += helper(v)
                
            if tmp == 0: 
                tmp = inf 
                
            return min(values[u], tmp)
            
        n = len(values)
        
        graph = defaultdict(lambda: [])
        
        for (u, v) in edges: 
            graph[u].append(v)
            graph[v].append(u)
            
        visited = {0}
        
        aSum = sum(values)
        
        return aSum - helper(0)
            
