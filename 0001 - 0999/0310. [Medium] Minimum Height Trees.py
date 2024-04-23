# https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2: 
            return {i for i in range(n)}
        
        degree = defaultdict(lambda: 0)
        graph = defaultdict(lambda: [])
        
        for (u, v) in edges: 
            degree[u] += 1 
            degree[v] += 1 
            
            graph[u].append(v)
            graph[v].append(u)
            
        stack = [i for i in range(n) if degree[i] == 1]    
        ans = {i for i in range(n) if degree[i] >= 2}
        
        while len(nodes) > 2: 
            newStack = []
            
            for u in stack: 
                for v in graph[u]:
                    degree[v] -= 1 
                    
                    if degree[v] == 1: 
                        newStack.append(v)
                        
                        ans.remove(v)
                        
            stack = newStack 
            
        return ans
        
